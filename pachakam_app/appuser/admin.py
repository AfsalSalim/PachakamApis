# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# # Register your models here.
from .models import *
from apis.models import Dish


class BookInline(admin.TabularInline):
	model = Kitchen

class DishInline(admin.TabularInline):
    model = Dish


class Useradmin(UserAdmin):
    inlines = [BookInline,]

class KitchenAdmin(admin.ModelAdmin):
    inlines = [DishInline,]

admin.site.register(AppUser, Useradmin)
admin.site.register(Kitchen, KitchenAdmin)
