from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

from models import Company, Platform, Genre, Game
from views import CompanyList, CompanyDetail, CompanyCreate, CompanyEdit, \
                CompanyDelete, \
                PlatformsList, PlatformDetail, PlatformCreate, PlatformEdit, \
                PlatformDelete, \
                GenresList,GenreDetail, GenreCreate, GenreEdit, GenreDelete, \
                GamesList, GameDetail, GameCreate, GameEdit, GameDelete,review, \
                APIGameList, APIGameReviewDetail, APIGameDetail, \
                APICompanyList, APICompanyDetail, APIPlatformList, \
                APIPlatformDetail, APIGenreList, APIGameReviewList, APIGenreDetail
from forms import CompanyForm, PlatformForm, GenreForm, GameForm

urlpatterns = [
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
        CompanyEdit.as_view(
            model=Company,
            form_class=CompanyForm),
        name='company_edit'),

    #Delete Company
    url(r'^companies/(?P<pk>\d+)/delete/$',
        CompanyDelete.as_view(),
        name='company_delete'),

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
        PlatformEdit.as_view(
            model=Platform,
            form_class=PlatformForm),
        name='platform_edit'),

    #Delete Platform
    url(r'^platforms/(?P<pk>\d+)/delete/$',
        PlatformDelete.as_view(),
        name='platform_delete'),

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
        GenreEdit.as_view(
            model=Genre,
            form_class=GenreForm),
        name='genre_edit'),

    #Delete Genre
    url(r'^genres/(?P<pk>\d+)/delete/$',
        GenreDelete.as_view(),
        name='genre_delete'),

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
        GameEdit.as_view(
            model=Game,
            form_class=GameForm),
        name='game_edit'),

    #Delete Game
    url(r'^games/(?P<pk>\d+)/delete/$',
        GameDelete.as_view(),
        name='game_delete'),

    # Create Review Game
     url(r'^games/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),

    # RESTful API
    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/games/$',
        APIGameList.as_view(), name='game-list'),
    url(r'^api/games/(?P<pk>\d+)/$',
        APIGameDetail.as_view(), name='game-detail'),

    url(r'^api/companies/$',
        APICompanyList.as_view(), name='companies-list'),
    url(r'^api/companies/(?P<pk>\d+)/$',
        APICompanyDetail.as_view(), name='company-detail'),

    url(r'^api/platforms/$',
        APIPlatformList.as_view(), name='platforms-list'),
    url(r'^api/platforms/(?P<pk>\d+)/$',
        APIPlatformDetail.as_view(), name='platform-detail'),

    url(r'^api/genres/$',
        APIGenreList.as_view(), name='genres-list'),
    url(r'^api/genres/(?P<pk>\d+)/$',
        APIGenreDetail.as_view(), name='genre-detail'),

    url(r'^api/gamereviews/$',
        APIGameReviewList.as_view(), name='gamereview-list'),
    url(r'^api/gamereviews/(?P<pk>\d+)/$',
        APIGameReviewDetail.as_view(), name='gamereview-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])
