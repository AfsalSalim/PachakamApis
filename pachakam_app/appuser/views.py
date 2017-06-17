# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from .models import *
from .serializers import *
from rest_framework import generics
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from apis.models import Dish
from apis.serializers import DishlistSerializer



class BookListView(generics.GenericAPIView):
    """
        View of list all the books based on the number of like for the dish
    """
    queryset = Book.objects.all().order_by("-like","dislike")
    serializer_class = BookListSerializer

    def get(self, request, *args, **kwargs):
        """
            Get request of the list the dishes
        """

        page_num = request.GET.get('page', 1)
        paginator = Paginator(self.get_queryset(), 1)
        try:
            paginated_entries = paginator.page(int(page_num))
        except PageNotAnInteger as e:
            paginated_entries = paginator.page(1)
        except EmptyPage:
            paginated_entries = paginator.page(paginator.num_pages)
        serializer = self.get_serializer(paginated_entries, many=True)
        if len(self.get_queryset()) > 0:
            if int(page_num) < paginator.num_pages:
                load_more_required = True
            else:
                load_more_required = False
            return Response({"status": "ok", "data": serializer.data,
                             "load_more_required": load_more_required})
        else:
            return Response({"status": "No books available",
                             "data": []})


class BookDetailed(generics.GenericAPIView):
    """
        view for listing the book based on the primary key
    """

    # serializer_class = BookDetailedSerializer

    def get(self, request, *args, ** kwargs):
        """
            Get method for detailed view for the dish
        """


        book_id = self.kwargs.get('book_pk')
        try:
            book = Book.objects.get(id=book_id)
            dishes = Dish.objects.filter(book=book)
            page_num = request.GET.get('page', 1)
            paginator = Paginator(dishes, 1)
            try:
                paginated_entries = paginator.page(int(page_num))
            except PageNotAnInteger as e:
                paginated_entries = paginator.page(1)
            except EmptyPage:
                paginated_entries = paginator.page(paginator.num_pages)
            # serializer = self.get_serializer(paginated_entries, many=True)
            serializer = DishlistSerializer(paginated_entries, many=True)
            if len(dishes) > 0:
                if int(page_num) < paginator.num_pages:
                    load_more_required = True
                else:
                    load_more_required = False
                return Response({"status": "ok", "data": serializer.data,
                             "load_more_required": load_more_required})
            else:
                return Response({"status": "No dishes availble in this book", "data":[]})
        except Book.DoesNotExist:
            return Response({"status": "No book with id exist",
                             "data": []})

