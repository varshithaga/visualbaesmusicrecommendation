# visualbasedmusicrecommendation
I have uploaded pdf regarding this project , steps,  database photo , postman and pictures related to it <br>
inside visualbasedmusicrecommendation folder

# create folder
<pre>
django-admin startproject visual_music_rec 
cd visual_music_rec
python manage.py startapp music
</pre>


# Environment
<pre>
cd ..
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
</pre>


# next steps

cd visual_music_rec <br>
create new folder named media which contains two folder genres_original(all music files based on genre) and uploaded_images(uploaded images for predicting genre and music based on genre)
take genre_original from below dataset <br>

dataset path --https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification<br>

create another file inside visua_music_rec folder named train_genre_cnn.py ( to train a CNN to classify music genres using your dataset)<br>
(here change the data directry path ) , this should contain images_original folder , the dataset from https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification   image_original folder is present inside this dataset)<br>

# Postgresql
install postgresql <br>
create a database named musicrecommend<br>
in settings.py <br>
and enter your  username and password in DATABASES

# training the model
next run in terminal (for training the model)<br>
python train_genre_cnn.py <br>
(to train the images)

# git clone
git clone the foldder <br>
https://github.com/varshithaga/visualbaesmusicrecommendation.git

# apply migrations
python manage.py makemigrations<br>
python manage.py migrate <br>


# next steps

create the folder named inside management<br>
inside create another folder named command <br>
inside that create a file named print_music_files.py  ( is to to automatically populate your MusicFile database table with information about the audio files from your dataset)<br>

# to run
then in terminal run --> <br>
python manage.py print_music_files<br>

# Final Run
python manage.py runserver





