from django.forms import ModelForm
from models import Company, Platform, Genre, Game

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ('user', 'date',)

class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        exclude = ('user', 'date',)

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        exclude = ('user', 'date',)

class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ('user', 'date',)
