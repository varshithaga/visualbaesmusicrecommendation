
from django.core.management.base import BaseCommand
from music.models import MusicFile
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Populate MusicFile table with audio files from dataset'

    def handle(self, *args, **kwargs):
        dataset_dir = os.path.join(settings.MEDIA_ROOT, 'genres_original')

        if not os.path.exists(dataset_dir):
            self.stdout.write(self.style.ERROR('Dataset directory does not exist!'))
            return

        for genre in os.listdir(dataset_dir):
            genre_path = os.path.join(dataset_dir, genre)
            if os.path.isdir(genre_path):
                audio_files = os.listdir(genre_path)
                for audio_file in audio_files:
                    # Relative path from MEDIA_ROOT
                    relative_path = os.path.join('genres_original', genre, audio_file).replace('\\', '/')
                    
                    # Save to DB
                    MusicFile.objects.create(
                        title=audio_file,
                        file_path=relative_path,  # relative path
                        genre=genre
                    )

        self.stdout.write(self.style.SUCCESS("Database population complete!"))
