# visualbaesmusicrecommendation
inside visualbasedmusicrecommendation folder

django-admin stratproject visual_music_rec

cd visual_music_rec  rty

python manage.py startapp music

to create environment
cd ..

python -m vev venv

.\venv\Scripts\activate

pip install -r requirements.txt

next steps

cd visual_music_rec

create new folder named media which contains two folder genres_original(all music files based on genre) and uploaded_images(uploaded images for predicting genre and music based on genre)

take genre_original from below dataset 

dataset path --https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

create another file inside visua_music_rec folder named train_genre_cnn.py ( to train a CNN to classify music genres using your dataset)
(here change the data directry path ) , this should contain images_original folder , the dataset from https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification   image_original folder is present inside this dataset)

install postgresql , 

create a database named musicrecommend

in settings.py 
and enter your  username and password in DATABASES

next run in terminal (for training the model)

python train_genre_cnn.py 
(to train the images)

git clone the folder and then apply migrations

python manage.py makemigrations

python manage.py migrate 


next 

create the folder named inside management
inside create another folder named command 
inside that create a file named print_music_files.py  ( is to to automatically populate your MusicFile database table with information about the audio files from your dataset)

then in terminal run --> python manage.py print_music_files

then run 
python manage.py runserver





