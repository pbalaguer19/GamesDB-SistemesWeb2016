from django.forms import ModelForm
from models import Company, Platform, Genre, Game

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ()

class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        exclude = ()

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        exclude = ()

class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ()
