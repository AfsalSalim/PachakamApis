from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^categories/$', ListCategories.as_view()),
    url(r'^categories/(?P<category_pk>[0-9]+)/$', CategoryDetailed.as_view()),
    url(r'^categories/(?P<category_pk>[0-9]+)/dishes$', ListDishes.as_view()),
    url(r'^categories/(?P<category_pk>[0-9]+)/dishes/(?P<dish_pk>[0-9]+)$', DishDetails.as_view()),
]