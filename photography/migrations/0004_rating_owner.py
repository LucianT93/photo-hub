# Generated by Django 4.1.1 on 2022-09-28 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_camera_updated_lens_updated_profile_updated'),
        ('photography', '0003_category_updated_photography_updated_rating_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]