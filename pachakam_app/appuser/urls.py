from django.urls import re_path

from .views import *

urlpatterns = [
    re_path(r'^list/$', BookListView.as_view()),
    # url(r'books/(?P<book_pk>[0-9]+)',BookDetailed.as_view())
]