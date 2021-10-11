#! /usr/bin/python3
from django.db import models

gender_choice = [
    ('male', 'male'),
    ('female', 'female'),
]
rated_choices = [
    ('G', 'G'),
    ('PG', 'PG'),
    ('R', 'R'),
    ('PG-13', 'PG-13'),
    ('NR', 'NR'),
]
genres_choice = [
    ('Horror', 'Horror'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Sports', 'Sports'),
    ('Comedy', 'Comedy'),
    ('Action', 'Action'),
    ('Romance', 'Romance'),
]
celeb_option = [
    ('actor', 'actor'),
    ('director', 'director'),
]


class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choice)
    bio = models.TextField()
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Movies(models.Model):
    title = models.CharField(max_length=25)
    
    #if date is after todays date then its coming soon, otherwise its released
    release_date = models.DateField()  
    rated = models.CharField(max_length=20, choices=rated_choices)
    is_prime = models.BooleanField(default=True)
    length = models.CharField(max_length=20)
    description = models.TextField()
    synopsis = models.TextField()
    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
    def __str__(self):
        return self.title

class Genres(models.Model):
    genres = models.CharField(max_length=10 ,choices=gender_choice)
    movies = models.ManyToManyField(Movies)
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

class MovieImages(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    cover_photo = models.BooleanField(default=True)
    image = models.ImageField()
    class Meta:
        verbose_name = 'MovieTrailer'
        verbose_name_plural = 'MovieTrailers'

class MovieTrailers(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    cover_trailer = models.BooleanField(default=True)
    trailer = models.FileField()
    class Meta:
        verbose_name = 'MovieImage'
        verbose_name_plural = 'MovieImages'

class Celebrity(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choice)
    bio = models.TextField()
    dob = models.DateField()
    type = models.CharField(max_length=10, choices=celeb_option)
    class Meta:
        verbose_name = 'Celebrity'
        verbose_name_plural = 'Celebrities'

class AssociatedMoveis(models.Model):
    movie = models.ManyToManyField(Movies)
    celeb = models.ManyToManyField(Celebrity)
    class Meta:
        verbose_name = 'AssociatedMovie'
        verbose_name_plural = 'AssociatedMovies'

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    movie = models.ManyToManyField(Movies)
    user = models.ManyToManyField(Users)
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Rating(models.Model):
    rating = models.FloatField()
    user = models.ManyToManyField(Users)
    movie = models.ManyToManyField(Movies)
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

class RecentlyViewedMovie(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    movie = models.ManyToManyField(Movies)
    user = models.ManyToManyField(Users)
    class Meta:
        verbose_name = 'RecentlyViewedMovie'
        verbose_name_plural = 'RecentlyViewedMovies'

class RecentlyViewedCeleb(models.Model):
    celeb = models.ManyToManyField(Celebrity)
    user = models.ManyToManyField(Users)
    class Meta:
        verbose_name = 'RecentlyViewedCeleb'
        verbose_name_plural = 'RecentlyViewedCelebs'

class BookmarkedMovies(models.Model):
    movie = models.ManyToManyField(Movies, related_name='users')
    user = models.ManyToManyField(Users, related_name='movies')
    date_time = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'BookmarkedMovie'
        verbose_name_plural = 'BookmarkedMovies'












