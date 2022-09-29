from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth import login, authenticate
from photography.forms import RatingForm, LoginForm
from photography.models import Photography, Rating


# Create your views here.


def photo_posts(request):
    all_photos = Photography.objects.all()
    form_rating = RatingForm()
    form_login = LoginForm()

    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST['username']
            password = request.POST['password']

            try:
                user = User.objects.get(username=username)
            except:
                print('Username does not exists')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
            else:
                print('Username or password incorrect!')
        else:
            form_rating = RatingForm(request.POST)
            photo_obj = Photography.objects.get(id=request.POST.get('photo_id'))
            rating = form_rating.save(commit=False)
            rating.photography = photo_obj
            rating.owner = request.user.profile
            rating.save()

    return render(request, 'home/home.html', {
        'all_photos': all_photos,
        'form_rating': form_rating,
        'form_login': form_login
    })
