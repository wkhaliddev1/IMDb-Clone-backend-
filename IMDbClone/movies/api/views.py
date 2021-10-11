from .serializers import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import viewsets
from ..models import (Users, Movies, Celebrity, MovieImages, Genres, 
                     MovieTrailers, AssociatedMoveis, Comment, 
                     Rating, RecentlyViewedMovie, RecentlyViewedCeleb,
                     BookmarkedMovies)
#JWT
from rest_framework_simplejwt.authentication import JWTAuthentication
#isAdmin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookmarkedMoviesView(viewsets.ModelViewSet):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookmarkedMovieSerializer
    queryset = BookmarkedMovies.objects.all()

class MovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movies.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

class CelebView(viewsets.ModelViewSet):
    serializer_class = CelebSerializer
    queryset = Celebrity.objects.all()

class MovieImagesView(viewsets.ModelViewSet):
    serializer_class = MovieImageSerializer
    queryset = MovieImages.objects.all()

class GenresView(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genres.objects.all()

class MovieTrailerView(viewsets.ModelViewSet):
    serializer_class = MovieTrailerSerializer
    queryset = MovieTrailers.objects.all()

class AssociatedMoviesCelebView(viewsets.ModelViewSet):
    serializer_class = AssociatedMoveiSerializer
    queryset = AssociatedMoveis.objects.all()

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class RatingView(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    class Meta:

        #A user can rate a movie only for once unlike comments
        validators = [UniqueTogetherValidator(
                          queryset = Rating.objects.all(),
                          fields = ['movie', 'user']
        )]

class RecentlyViewedMovieView(viewsets.ModelViewSet):
    serializer_class = RecentlyViewedMovieSerializer
    queryset = RecentlyViewedMovie.objects.all()

class RecentlyViewedCelebView(viewsets.ModelViewSet):
    serializer_class = RecentlyViewedCelebSerializer
    queryset = RecentlyViewedCeleb.objects.all()



