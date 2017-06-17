from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^books/$', BookListView.as_view()),
    url(r'books/(?P<book_pk>[0-9]+)',BookDetailed.as_view())
]