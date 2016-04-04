from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import TemplateView

from models import Company
from views import CompanyList, CompanyDetail, PlatformsList, PlatformDetail

urlpatterns = patterns('',

    # Home page
    url(r'^$',
        TemplateView.as_view(template_name="gamesApp/main.html"),
        name="Home"),

    # Company list
    url(r'^companies\.(?P<extension>(json|xml|html))$',
        CompanyList.as_view(),
        name='companies_list'),

    # Company details
    url(r'^companies/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        CompanyDetail.as_view(),
        name='company_detail'),

    # Platforms list
    url(r'^platforms\.(?P<extension>(json|xml|html))$',
        PlatformsList.as_view(),
        name='platforms_list'),

    # Platform details
    url(r'^platforms/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        PlatformDetail.as_view(),
        name='platform_detail'),

)
