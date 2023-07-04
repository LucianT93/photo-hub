from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView

from equipment.forms import LensForm
from photography.forms import CreatePostPhoto
from users.forms import ProfileForm
from users.models import Profile


def profile_detail(request):
    profile = request.user.profile
    lens_form = LensForm()
    profile_form = ProfileForm(instance=profile)
    profile = Profile.objects.get(id=request.user.profile.id)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    return render(request, 'users/profile.html',
                  {'profile': profile,
                   'form': lens_form,
                   'profile_form': profile_form,
                   'form_create_photo': CreatePostPhoto()})

