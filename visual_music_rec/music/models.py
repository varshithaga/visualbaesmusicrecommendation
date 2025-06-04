from django.db import models
from django.contrib.auth.models import User

class UploadedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True, related_name='uploaded_images_user')  
    image = models.ImageField(upload_to='uploaded_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MusicRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,  related_name='music_recommendations_user') 
    image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE,null=True,blank=True,  related_name='music_recommendations_image')
    music_file_path = models.CharField(max_length=255)
    similarity_score = models.FloatField(null=True, blank=True)

class MusicFile(models.Model):
    title = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)  
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title