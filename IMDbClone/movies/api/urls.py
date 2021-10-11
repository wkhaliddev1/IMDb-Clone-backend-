from django.db.models import base
from django.urls.resolvers import URLPattern
from .views import BookmarkedMoviesView, MovieView, UserView, MovieImagesView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('bookmarked-movies', BookmarkedMoviesView, basename = 'bookmarkedMovies')
router.register('movies', MovieView, basename = 'movies')
router.register('users', UserView, basename = 'users')
router.register('movies-images', UserView, basename = 'moviesImage')

urlpatterns = [
    path('', include(router.urls))
]