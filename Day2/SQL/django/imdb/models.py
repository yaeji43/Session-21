from django.db import models

# Create your models here.


class ImdbDirectors(models.Model):
    director_id = models.BigIntegerField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'imdb_directors'


class ImdbMovies(models.Model):
    movie_id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'imdb_movies'

class ImdbMoviesDirectors(models.Model):
    movie_id = models.ForeignKey(ImdbMovies, on_delete=models.CASCADE)
    director_id = models.ForeignKey(ImdbDirectors, on_delete=models.CASCADE)
    class Meta:
        db_table = 'imdb_movies_directors'

class ImdbMoviesGenre(models.Model):
    movie_id = models.ForeignKey(ImdbMovies, on_delete=models.CASCADE)
    genre = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'imdb_movies_genre'
