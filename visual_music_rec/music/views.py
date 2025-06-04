# def index(request):
#     if request.method == 'POST' and request.FILES['image']:
#         if not request.user.is_authenticated:
#             # Redirect or return error - user must log in
#             return redirect('login')

#         image = request.FILES['image']
#         uploaded_image = UploadedImage.objects.create(user=request.user, image=image)
#         uploaded_image.save()

#         # Generate recommendations as before
#         image_path = uploaded_image.image.path
#         top_10_music = find_best_fit_music(image_path)

#         # Save recommendations
#         for music_path, score in top_10_music:
#             MusicRecommendation.objects.create(
#                 image=uploaded_image,
#                 music_file_path=music_path,
#                 similarity_score=score
#             )

#         recommendations = uploaded_image.recommendations.all()

#         return render(request, 'music/index.html', {
#             'image_url': uploaded_image.image.url,
#             'recommendations': recommendations
#         })

#     return render(request, 'music/index.html')


# from django.shortcuts import render, redirect
# from .forms import ImageUploadForm

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('upload_success')  # Redirect after successful upload
#     else:
#         form = ImageUploadForm()
#     return render(request, 'music/upload_image.html', {'form': form})

# def upload_success(request):
#     return render(request, 'music/upload_success.html')


# def home(request):
#     return render(request, 'music/home.html')


import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import UploadedImage  
from .forms import ImageUploadForm
import tensorflow as tf  
from .models import MusicFile,MusicRecommendation 

# Load the model once globally to avoid reloading every request
MODEL_PATH = os.path.join(settings.BASE_DIR, 'genre_cnn_model.h5')
model = load_model(MODEL_PATH)

# Map class indices to genre names
CLASS_NAMES = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            image_instance.user = request.user  
            image_instance.save()
            return redirect('predict_genre', pk=image_instance.pk)
    else:
        form = ImageUploadForm()
    return render(request, 'music/upload_image.html', {'form': form})

def predict_genre(request, pk):
    image_instance = get_object_or_404(UploadedImage, pk=pk)
    img_path = image_instance.image.path

    user_id = image_instance.user.id if image_instance.user else None

    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    predicted_genre = CLASS_NAMES[predicted_index]

    top_10_songs = MusicFile.objects.filter(genre=predicted_genre).order_by('?')[:10]

    # Save new recommendations to the MusicRecommendation model
    for song in top_10_songs:
        MusicRecommendation.objects.create(
            user=image_instance.user,
            image=image_instance,
            music_file_path=song.file_path,
        )

    return render(request, 'music/prediction_result.html', {
        'predicted_genre': predicted_genre,
        'image_url': image_instance.image.url,
        'songs': top_10_songs,
        'MEDIA_URL': settings.MEDIA_URL, 
        'user_id': user_id,  
    })

def home(request):
    return render(request, 'music/home.html')


