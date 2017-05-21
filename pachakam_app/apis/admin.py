# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *

## Registering all the tables to admin site


class IngridientListInline(admin.TabularInline):
    model = IngridientList

class GalleryAdmin(admin.ModelAdmin):
    inlines = [ IngridientListInline, ]
    # model = Dish


admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Dish,GalleryAdmin)
admin.site.register(Ingridient)
admin.site.register(IngridientList)
admin.site.register(step)
