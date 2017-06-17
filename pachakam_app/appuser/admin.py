# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *
# from apis.models import Dish


class BookInline(admin.TabularInline):
	model = Book



class Useradmin(UserAdmin):
    inlines = [BookInline,]

admin.site.register(AppUser, Useradmin)
admin.site.register(Book)
