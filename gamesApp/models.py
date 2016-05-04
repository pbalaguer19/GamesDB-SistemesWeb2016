from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.

class Company(models.Model):
    name = models.TextField()
    abbreviation = models.TextField(blank=True, null=True)
    city = models.TextField(max_length=100, blank=True, null=True)
    mail = models.TextField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('gamesApp:company_detail', kwargs={'pk': self.pk})

class Platform(models.Model):
    name = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('gamesApp:platform_detail', kwargs={'pk': self.pk})

class Genre(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('gamesApp:genre_detail', kwargs={'pk': self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'),\
    (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', default=3,\
    choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    publish_date = models.DateField(default=date.today)
    user = models.ForeignKey(User, default=1)

class Game(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    companies = models.ManyToManyField(Company, related_name="games")
    platforms = models.ManyToManyField(Platform, related_name="games")
    genres = models.ManyToManyField(Genre, related_name="games")

    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('gamesApp:game_detail', kwargs={'pk': self.pk})

class GameReview(Review):
    game = models.ForeignKey(Game)
    def __unicode__(self):
        return u"Review %s" % self.game.name
