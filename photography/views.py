import json
import time

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth import login, authenticate, logout
from photography.forms import RatingForm, LoginForm, SignUpForm
from photography.models import Photography, Rating


class PhotoPostHome(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        data = super(PhotoPostHome, self).get_context_data(**kwargs)
        all_photos = Photography.objects.all().order_by('-created')
        form_rating = RatingForm()
        form_login = LoginForm()
        form_signup = SignUpForm()

        data['form_rating'] = form_rating
        data['form_login'] = form_login
        data['form_signup'] = form_signup
        data['all_photos'] = all_photos

        return data


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
    if form_signup.is_valid() and not form_signup.errors:
        user = form_signup.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, authenticate(
            username=form_signup.cleaned_data['username'], password=form_signup.cleaned_data['password1']))
        return HttpResponse(json.dumps({'message': 'success'}), content_type='application/json')
    return HttpResponse(json.dumps({"message": "denied"}), content_type="application/json")


def rating_form(request):
    form_rating = RatingForm(request.POST)
    photo_obj = Photography.objects.get(id=request.POST.get('photo_id'))
    if form_rating.is_valid():
        rating = form_rating.save(commit=False)
        rating.photography = photo_obj
        rating.owner = request.user.profile
        rating.save()
    return redirect('home')
