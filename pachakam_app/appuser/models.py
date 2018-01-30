# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AppUser(AbstractUser):

    """
        Define fields related to a user
    """

    google_access_token = models.CharField(max_length=100, default=None, null=True, blank=True)
    facebook_access_token = models.CharField(max_length=100, default=None, null=True, blank=True)
    google_uid = models.CharField(max_length=100, default=None, null=True, blank=True)
    facebook_uid = models.CharField(max_length=100, default=None, null=True, blank=True)


    def __str__(self):
        
        """ 
            return the display name
        """
        return str(self.username)

    class Meta:
        
        """ 
            Meta
        """
        verbose_name = 'AppUser'
        verbose_name_plural = 'AppUsers'




class Kitchen(models.Model):

    """
        Model for the book details of the user
    """

    name = models.CharField(max_length=100)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):

        """
            Returns the display of the book
        """

        return self.name

    class Meta:
        """
            Meta
        """
        unique_together = ('name', 'user')

