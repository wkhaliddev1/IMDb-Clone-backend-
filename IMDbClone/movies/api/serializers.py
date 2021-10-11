from rest_framework import serializers
from ..models import (Users, Movies, Celebrity, MovieImages, Genres, 
                     MovieTrailers, AssociatedMoveis, Comment, 
                     Rating, RecentlyViewedMovie, RecentlyViewedCeleb,
                     BookmarkedMovies)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class BookmarkedMovieSerializer(serializers.ModelSerializer): 

    #BookmarkedMoves has FK of Users Model and Movies Model
    user = UserSerializer(many=True)
    movie = MovieSerializer(many=True)
    
    # user = UserSerializer()  this should work
    # movie = MovieSerializer()
    class Meta:
        model = BookmarkedMovies
        fields = '__all__'

class CelebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity

class MovieImageSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    class Meta:
        model = MovieImages
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Genres

class MovieTrailerSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    class Meta:
        model = MovieTrailers

class AssociatedMoveiSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    celeb = CelebSerializer(many=True)
    class Meta:
        model = AssociatedMoveis

class CommentSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    user = UserSerializer(many=True)
    class Meta:
        model = Comment

class RatingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    user = UserSerializer(many=True)
    class Meta:
        model = Rating

class RecentlyViewedMovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    user = UserSerializer(many=True)
    class Meta:
        model = RecentlyViewedMovie

class RecentlyViewedCelebSerializer(serializers.ModelSerializer):
    celeb = CelebSerializer(many=True)
    user = UserSerializer(many=True)
    class Meta:
        model = RecentlyViewedCeleb



