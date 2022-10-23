import uuid

from django.db import models
from users.models import Profile

# Create your models here.


class Photography(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    image = models.ImageField()
    up_votes = models.IntegerField(default=0, null=True, blank=True)
    down_votes = models.IntegerField(default=0, null=True, blank=True)
    category = models.ManyToManyField('Category')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    photography = models.ForeignKey(Photography, on_delete=models.CASCADE)
    body = models.TextField(max_length=400, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.body


class RatingLikeDislike(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    photography = models.ForeignKey(Photography, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
