import time

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth import login, authenticate, logout
from photography.forms import RatingForm, LoginForm, SignUpForm
from photography.models import Photography, Rating


# Create your views here.


# def photo_posts(request):
#     all_photos = Photography.objects.all()
#     form_rating = RatingForm()
#     form_login = LoginForm()
#     form_signup = SignUpForm()
#
#     if request.method == 'POST':
#         if request.POST.get('username') and request.POST.get('password'):
#             username = request.POST['username']
#             password = request.POST['password']
#
#             try:
#                 user = User.objects.get(username=username)
#             except:
#                 messages.error(request, 'Username does not exists')
#
#             user = authenticate(request, username=username, password=password)
#
#             if user:
#                 login(request, user)
#                 messages.success(request, 'Logged it successfully ')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Username or password incorrect!')
#         elif request.POST.get('value') and request.POST.get('body'):
#             form_rating = RatingForm(request.POST)
#             photo_obj = Photography.objects.get(id=request.POST.get('photo_id'))
#             if form_rating.is_valid():
#                 rating = form_rating.save(commit=False)
#                 rating.photography = photo_obj
#                 rating.owner = request.user.profile
#                 rating.save()
#         else:
#             print(request.POST)
#             form_signup = SignUpForm(request.POST)
#             if form_signup.is_valid():
#                 user = form_signup.save(commit=False)
#                 user.username = user.username.lower()
#                 user.save()
#                 messages.success(request, 'User account was created! ')
#
#     return render(request, 'home/home.html', {
#         'all_photos': all_photos,
#         'form_rating': form_rating,
#         'form_login': form_login,
#         'form_signup': form_signup,
#     })

class PhotoPostHome(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        all_photos = Photography.objects.all().order_by('-created')
        form_rating = RatingForm()
        form_login = LoginForm()
        form_signup = SignUpForm()

        return self.render_to_response({
            'form_rating': form_rating,
            'form_login': form_login,
            'form_signup': form_signup,
            'all_photos': all_photos
        })

    def post(self, request, *args, **kwargs):
        if request.POST.get('form_login') == 'f_login':
            username = request.POST['username']
            password = request.POST['password']

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'Username does not exists')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Logged it successfully ')
                return redirect('home')
            else:
                messages.error(request, 'Username or password incorrect!')
                return redirect('home')

        if request.POST.get('form_signup') == 'f_signup':
            form_signup = SignUpForm(request.POST)
            if form_signup.is_valid():
                user = form_signup.save(commit=False)
                user.username = user.username.lower()
                user.save()
                messages.success(request, 'User account was created! ')
            return redirect('home')
        if request.POST.get('form_rating') == 'f_rating':
            form_rating = RatingForm(request.POST)
            photo_obj = Photography.objects.get(id=request.POST.get('photo_id'))
            if form_rating.is_valid():
                rating = form_rating.save(commit=False)
                rating.photography = photo_obj
                rating.owner = request.user.profile
                rating.save()
            return redirect('home')


def logoutUser(request):
    logout(request)
    return redirect('home')
