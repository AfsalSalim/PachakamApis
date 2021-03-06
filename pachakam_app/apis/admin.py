# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib import admin

# # Register your models here.

from .models import *

# ## Registering all the tables to admin site


class IngridientListInline(admin.TabularInline):
    model = Ingridient

class StepInline(admin.TabularInline):
	model = step

class GalleryAdmin(admin.ModelAdmin):
    inlines = [ IngridientListInline, StepInline]
    model = Dish


# # admin.site.register(Category)
# # admin.site.register(Unit)
admin.site.register(Dish,GalleryAdmin)
admin.site.register(Ingridient)
