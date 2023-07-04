from django.shortcuts import render, redirect

from equipment.models import Camera, Lens


# Create your views here.

def get_camera(request):
    if request.method == 'POST':
        camera = Camera.objects.create(
            profile=request.user.profile,
            name=request.POST.get('camera')
        )
        camera.save()
    return redirect('profile')


def get_lens(request):
    camera = Camera.objects.get(id=request.POST.get('camera'))
    if request.method == 'POST':
        lens = Lens.objects.create(
            camera=camera,
            name=request.POST.get('lens')
        )
        lens.save()
    return redirect('profile')
