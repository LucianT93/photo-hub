from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView
from users.forms import ProfileForm, CameraForm, LensForm
from users.models import Profile


class ProfileDetail(LoginRequiredMixin, DetailView):
    template_name = 'users/profile.html'
    model = Profile


def update_profile(request, pk):
    profile = request.user.profile
    profile_form = ProfileForm(instance=profile)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    return render(
        request,
        'users/update_profile.html',
        {'profile': profile, 'profile_form': profile_form}
    )
