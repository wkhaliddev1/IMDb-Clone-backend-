from django.contrib import admin
from .models import (Users, Movies, Celebrity, MovieImages, Genres, 
                     MovieTrailers, AssociatedMoveis, Comment, 
                     Rating, RecentlyViewedMovie, RecentlyViewedCeleb,
                     BookmarkedMovies)

@admin.register(Users, Movies, Celebrity, Genres, MovieTrailers,
                AssociatedMoveis, Comment, Rating, RecentlyViewedMovie,
                RecentlyViewedCeleb, BookmarkedMovies)
class UserAdmin(admin.ModelAdmin):
    pass
    #model = BookmarkedMovies
    #raw_id_fields = ['movie', 'user']

@admin.register(MovieImages)
class MovieImageAdmin(admin.ModelAdmin):
    model = MovieImages
    list_display = ('movie', 'cover_photo', 'image')
        
    





