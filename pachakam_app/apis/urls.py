from django.urls import re_path

from .views import *

urlpatterns = [
    re_path(r'(?P<book_pk>[0-9]+)/dishes',ListDishes.as_view()),
    re_path(r'dishes/(?P<dish_pk>[0-9]+)',DishDetailed.as_view()),
    # re_path(r'add_kitchen/$', AddKitchen.as_view())
]