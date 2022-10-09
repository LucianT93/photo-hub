import datetime

import requests
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from users.models import Profile


def profile_view(request, pk):
    profile = Profile.objects.get(id=pk)
    elapsed_times = []
    for photo in profile.photography_set.all():
        elapsed_times.append(datetime.datetime.now() - photo.updated.replace(tzinfo=None))

    return render(request, 'users/profile.html', {'profile': profile, 'photo_elapsed_times': elapsed_times})


