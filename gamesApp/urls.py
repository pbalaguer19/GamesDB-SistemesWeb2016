from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import TemplateView

from models import Company, Platform, Genre, Game
from views import CompanyList, CompanyDetail, CompanyCreate,\
                PlatformsList, PlatformDetail, PlatformCreate,\
                GenresList,GenreDetail, GenreCreate, \
                GamesList, GameDetail, GameCreate
from forms import CompanyForm, PlatformForm, GenreForm, GameForm

urlpatterns = patterns('',

    # Home page
    url(r'^$',
        TemplateView.as_view(template_name="gamesApp/main.html"),
        name="Home"),

    # Company list
    url(r'^companies\.(?P<extension>(json|xml|html))?$',
        CompanyList.as_view(),
        name='companies_list'),

    # Company details
    url(r'^companies/(?P<pk>\d+)\.(?P<extension>(json|xml|html))?$',
        CompanyDetail.as_view(),
        name='company_detail'),

    # Create Company
    url(r'^companies/create/$',
        CompanyCreate.as_view(),
        name='company_create'),

    # Edit Company
    url(r'^companies/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Company,
            template_name='gamesApp/company_form.html',
            form_class=CompanyForm),
        name='company_edit'),

    # Platforms list
    url(r'^platforms\.(?P<extension>(json|xml|html))?$',
        PlatformsList.as_view(),
        name='platforms_list'),

    # Platform details
    url(r'^platforms/(?P<pk>\d+)\.(?P<extension>(json|xml|html))?$',
        PlatformDetail.as_view(),
        name='platform_detail'),

    # Create Platform
    url(r'^platforms/create/$',
        PlatformCreate.as_view(),
        name='platform_create'),

    # Edit Platform
    url(r'^platforms/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Platform,
            template_name='gamesApp/platform_form.html',
            form_class=PlatformForm),
        name='platform_edit'),

    # Genres list
    url(r'^genres\.(?P<extension>(json|xml|html))?$',
        GenresList.as_view(),
        name='genres_list'),

    # Genre details
    url(r'^genres/(?P<pk>\d+)\.(?P<extension>(json|xml|html))?$',
        GenreDetail.as_view(),
        name='genre_detail'),

    # Create Genre
    url(r'^genres/create/$',
        GenreCreate.as_view(),
        name='genre_create'),

    # Edit Genre
    url(r'^genres/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Genre,
            template_name='gamesApp/form.html',
            form_class=GenreForm),
        name='genre_edit'),

    # Games list
    url(r'^games\.(?P<extension>(json|xml|html))?$',
        GamesList.as_view(),
        name='games_list'),

    # Game details
    url(r'^games/(?P<pk>\d+)\.(?P<extension>(json|xml|html))?$',
        GameDetail.as_view(),
        name='game_detail'),

    # Create Game
    url(r'^games/create/$',
        GameCreate.as_view(),
        name='game_create'),

    # Edit Game
    url(r'^games/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Game,
            template_name='gamesApp/form.html',
            form_class=GameForm),
        name='game_edit'),
)
