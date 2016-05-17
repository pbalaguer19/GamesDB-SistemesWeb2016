from rest_framework.fields import CharField, DateField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Game, Company, Platform, Genre, GameReview


class GamesSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='gamesApp:game-detail')
    companies = HyperlinkedRelatedField(many=True,queryset=Company.objects.all(), view_name='gamesApp:company-detail')
    platforms = HyperlinkedRelatedField(many=True, queryset=Platform.objects.all(), view_name='gamesApp:platform-detail')
    genres = HyperlinkedRelatedField(many=True, queryset=Genre.objects.all(), view_name='gamesApp:genre-detail')
    gamereview_set = HyperlinkedRelatedField(many=True, read_only=True,
                                                   view_name='gamesApp:gamereview-detail')
    user = CharField(read_only=True)
    date = DateField(read_only=True)

    class Meta:
        model = Game
        fields = ('uri', 'name', 'description', 'release_year', 'website', 'companies', 'platforms',
                  'genres', 'user', 'date', 'gamereview_set')

class CompanySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='gamesApp:company-detail')
    games = HyperlinkedRelatedField(many=True, view_name='gamesApp:game-detail', read_only=True)
    user = CharField(read_only=True)
    date = DateField(read_only=True)

    class Meta:
        model = Company
        fields = ('uri', 'name', 'abbreviation', 'country', 'city', 'mail', 'website',
        'user', 'date', 'games')

class PlatformSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='gamesApp:platform-detail')
    games = HyperlinkedRelatedField(many=True, view_name='gamesApp:game-detail', read_only=True)
    user = CharField(read_only=True)
    date = DateField(read_only=True)

    class Meta:
        model = Platform
        fields = ('uri', 'name', 'price', 'release_year', 'user', 'date', 'games')

class GenreSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='gamesApp:genre-detail')
    games = HyperlinkedRelatedField(many=True, view_name='gamesApp:game-detail', read_only=True)
    user = CharField(read_only=True)
    date = DateField(read_only=True)

    class Meta:
        model = Genre
        fields = ('uri', 'name', 'description', 'user', 'date', 'games')


class GameReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='gamesApp:gamereview-detail')
    game = HyperlinkedRelatedField(view_name='gamesApp:game-detail', read_only=True)
    user = CharField(read_only=True)
    date = DateField(read_only=True)

    class Meta:
        model = GameReview
        fields = ('uri', 'rating', 'comment', 'user', 'publish_date', 'game')
