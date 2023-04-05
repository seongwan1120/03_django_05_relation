from django.db import models

# from datetime import datetime

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=300)
    debut = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.pk}: {self.name}'

class Album(models.Model):
    title = models.CharField(max_length=300)
    release_date = models.DateField()
    sell_amount = models.PositiveIntegerField()
    artists = models.ManyToManyField(Artist, related_name='albums')  # album_set을 albums로 변경.

    def __str__(self):
        return f'{self.pk}: {self.title}'

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk}: {self.title}'
    
'''
artist1 = Artist.objects.get(pk=1)
artist2 = Artist.objects.get(pk=2)

album1 = Album.objects.get(pk=4)
album1 = Album.objects.last()

album1.artists.add(artist1)
album1.artists.add(artist2)

album1.artists.remove(artist2)

album1.artists.all()  # [artist1, artist2], 앨범1에 참여한 모든 아티스트. 정참조.

artist1.album_set.all()  # 아티스트1이 참여한 모든 앨범. 역참조

artist1.albums.all()  # related name. 역참조의 형태 변경.
'''