from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Game, Company, Platform, Genre


class GamesSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='gamesApp:game-detail')
    companies = HyperlinkedRelatedField(many=True, read_only=True, view_name='gamesApp:company-detail')
    platforms = HyperlinkedRelatedField(many=True, read_only=True, view_name='gamesApp:platform-detail')
    genres = HyperlinkedRelatedField(many=True, read_only=True, view_name='gamesApp:genre-detail')
    gamereview_set = HyperlinkedRelatedField(many=True, read_only=True,
                                                   view_name='gamesApp:gamereview-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Game
        fields = ('uri', 'name', 'description', 'release_year', 'website', 'companies', 'platforms',
                  'genres', 'user', 'date', 'gamereview_set')
