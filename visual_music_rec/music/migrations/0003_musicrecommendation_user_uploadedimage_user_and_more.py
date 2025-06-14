# Generated by Django 4.2.21 on 2025-06-03 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0002_musicfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicrecommendation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='music_recommendations_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='uploadedimage',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_images_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='musicrecommendation',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='music_recommendations_image', to='music.uploadedimage'),
        ),
    ]
