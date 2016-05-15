from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, UpdateView

from rest_framework import generics, permissions

from models import Company, Platform, Genre, Game, GameReview
from forms import CompanyForm, PlatformForm, GenreForm, GameForm
from serializers import GamesSerializer, CompanySerializer, PlatformSerializer, \
                    GenreSerializer, GameReviewSerializer


class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)

class CompanyList(ListView, ConnegResponseMixin):
    model = Company
    template_name = 'gamesApp/companies_list.html'
    context_object_name = 'latest_companies_list'

class CompanyDetail(DetailView, ConnegResponseMixin):
    model = Company
    template_name = 'gamesApp/company_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetail, self).get_context_data(**kwargs)
        return context

class CompanyCreate(CreateView):
    model = Company
    template_name = 'gamesApp/company_form.html'
    form_class = CompanyForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CompanyCreate, self).form_valid(form)

class PlatformsList(ListView, ConnegResponseMixin):
    model = Platform
    template_name = 'gamesApp/platforms_list.html'
    context_object_name = 'latest_platforms_list'

class PlatformDetail(DetailView, ConnegResponseMixin):
    model = Platform
    template_name = 'gamesApp/platform_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PlatformDetail, self).get_context_data(**kwargs)
        return context

class PlatformCreate(CreateView):
    model = Platform
    template_name = 'gamesApp/platform_form.html'
    form_class = PlatformForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlatformCreate, self).form_valid(form)

class GenresList(ListView, ConnegResponseMixin):
    model = Genre
    template_name = 'gamesApp/genres_list.html'
    context_object_name = 'latest_genres_list'

class GenreDetail(DetailView, ConnegResponseMixin):
    model = Genre
    template_name = 'gamesApp/genre_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GenreDetail, self).get_context_data(**kwargs)
        return context

class GenreCreate(CreateView):
    model = Genre
    template_name = 'gamesApp/genre_form.html'
    form_class = GenreForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GenreCreate, self).form_valid(form)

class GamesList(ListView, ConnegResponseMixin):
    model = Game
    template_name = 'gamesApp/games_list.html'
    context_object_name = 'latest_games_list'

class GameDetail(DetailView, ConnegResponseMixin):
    model = Game
    template_name = 'gamesApp/game_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GameDetail, self).get_context_data(**kwargs)
        return context

class GameCreate(CreateView):
    model = Game
    template_name = 'gamesApp/game_form.html'
    form_class = GameForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GameCreate, self).form_valid(form)

#*********** RESTful ***********#

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class APIGameList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Game
    queryset = Game.objects.all()
    serializer_class = GamesSerializer

class APIGameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Game
    queryset = Game.objects.all()
    serializer_class = GamesSerializer

class APICompanyList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Company
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class APICompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Company
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class APIPlatformList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Platform
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class APIPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Platform
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class APIGenreList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Genre
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class APIGenreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Genre
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class APIGameReviewList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = GameReview
    queryset = GameReview.objects.all()
    serializer_class = GameReviewSerializer

class APIGameReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = GameReview
    queryset = GameReview.objects.all()
    serializer_class = GameReviewSerializer
