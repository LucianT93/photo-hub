# Generated by Django 4.1.1 on 2022-10-15 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location'),
        ('photography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photography',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
