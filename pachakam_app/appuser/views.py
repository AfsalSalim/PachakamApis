# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render

# # Create your views here.

from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response



class BookListView(generics.GenericAPIView):
    """
        View of list all the books based on the number of like for the dish
    """
    queryset = Kitchen.objects.all().order_by("-like","dislike")
    serializer_class = BookListSerializer

    def get(self, request, *args, **kwargs):
        """
            Get request of the list the dishes
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({"status": 1, "data": serializer.data})


