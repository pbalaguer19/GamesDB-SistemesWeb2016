from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView

from models import Company, Platform, Genre, Game

class CompanyList(ListView):
    model = Company
    template_name = 'gamesApp/companies_list.html'
    context_object_name = 'latest_companies_list'

class CompanyDetail(DetailView):
    model = Company
    template_name = 'gamesApp/company_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetail, self).get_context_data(**kwargs)
        return context

class PlatformsList(ListView):
    model = Platform
    template_name = 'gamesApp/platforms_list.html'
    context_object_name = 'latest_platforms_list'

class PlatformDetail(DetailView):
    model = Platform
    template_name = 'gamesApp/platform_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PlatformDetail, self).get_context_data(**kwargs)
        return context

class GenresList(ListView):
    model = Genre
    template_name = 'gamesApp/genres_list.html'
    context_object_name = 'latest_genres_list'

class GenreDetail(DetailView):
    model = Genre
    template_name = 'gamesApp/genre_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GenreDetail, self).get_context_data(**kwargs)
        return context

class GamesList(ListView):
    model = Game
    template_name = 'gamesApp/games_list.html'
    context_object_name = 'latest_games_list'

class GameDetail(DetailView):
    model = Game
    template_name = 'gamesApp/game_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GameDetail, self).get_context_data(**kwargs)
        return context
