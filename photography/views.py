import json
import time

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth import login, authenticate, logout
from photography.forms import CreateProfileOnRegister, CommentForm, CreatePostPhoto
from photography.models import Photography, RatingLikeDislike
from users.forms import LoginForm, SignUpForm


def photo_post_home(request):
    if request.method == 'POST':
        photo_obj = Photography.objects.get(id=request.POST.get('photo_id'))
        owner = request.user.profile
        if request.POST.get('like'):
            like_obj = RatingLikeDislike(name='Like', owner=owner, photography=photo_obj)
            like_obj.save()
            photo_obj.up_votes += 1
            photo_obj.save()
            # TODO: like button remains disabled if already voted -> html
        else:
            dislike_obj = RatingLikeDislike(name='Dislike', owner=owner, photography=photo_obj)
            dislike_obj.save()
            photo_obj.down_votes += 1
            photo_obj.save()
    context = {
        'form_comment': CommentForm(),
        'form_login': LoginForm(),
        'form_signup': SignUpForm(),
        'form_create_photo': CreatePostPhoto(),
        'all_photos': Photography.objects.all().order_by('-created')
    }
    return render(request, 'home/home.html', context)


# def get_like_owners(request, pk):
#     photo = Photography.objects.get(id=pk)
#     if request.user in [rating.owner.user for rating in photo.ratinglikedislike_set.all()]:
#         return HttpResponse(json.dumps({'message': 'already liked'}), content_type='application/json')
#     return HttpResponse(json.dumps({'message': 'not liked'}), content_type='application/json')


def user_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return HttpResponse(json.dumps({'message': 'success'}), content_type='application/json')
    return HttpResponse(json.dumps({"message": "denied"}), content_type="application/json")


def user_register(request):
    form_signup = SignUpForm(request.POST)
    auto_profile_form = CreateProfileOnRegister()
    if form_signup.is_valid() and not form_signup.errors:
        new_user = form_signup.save(commit=False)
        new_profile = auto_profile_form.save(commit=False)
        new_user.username = new_user.username.lower()
        new_profile.user = new_user
        new_user.save()
        new_profile.save()
        login(request, authenticate(
            username=form_signup.cleaned_data['username'], password=form_signup.cleaned_data['password1']))
        return HttpResponse(json.dumps({'message': 'success'}), content_type='application/json')
    return HttpResponse(json.dumps({"message": "denied"}), content_type="application/json")


def comment_form(request):
    form_comment = CommentForm(request.POST)
    photo_obj = Photography.objects.get(id=request.POST.get('photo_id'))
    if form_comment.is_valid():
        rating = form_comment.save(commit=False)
        rating.photography = photo_obj
        rating.owner = request.user.profile
        rating.save()
    return redirect('home')


def create_post(request):
    if request.method == 'POST':
        post_form = CreatePostPhoto(request.POST, request.FILES)
        if post_form.is_valid():
            photo_post = post_form.save(commit=False)
            photo_post.owner = request.user.profile
            photo_post.save()
    return redirect('home')
