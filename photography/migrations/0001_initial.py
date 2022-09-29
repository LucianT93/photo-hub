# Generated by Django 4.1.1 on 2022-09-29 11:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photography',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=400)),
                ('image', models.ImageField(upload_to='')),
                ('up_votes', models.IntegerField(blank=True, default=0, null=True)),
                ('down_votes', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.ManyToManyField(to='photography.category')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('body', models.TextField(blank=True, max_length=400, null=True)),
                ('value', models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike')], max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('photography', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photography.photography')),
            ],
        ),
    ]
