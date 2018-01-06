# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render

from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# # Create your views here.


class ListDishes(generics.GenericAPIView):

    """
        View for listing all the dishes under current catgories
    """

    serializer_class = DishlistSerializer

    def get(self,request, *args, **kwargs):

        """
            Get method for list dihes
        """

        category_id = self.kwargs.get('book_pk')
        dishes = Dish.objects.filter(book__id=category_id)
        serializer = self.get_serializer(dishes, many=True)
        return Response({"status":1, "data": serializer.data})


class DishDetailed(generics.GenericAPIView):

    """
        View for detailed data for the current category  and dish
    """

    serializer_class = DishDetialsSerializer

    def get(self, request, *args, **kwargs):

        """
            Get method for the view
        """

        try:
            dish_id = self.kwargs.get('dish_pk')
            dish = Dish.objects.get(id=dish_id)
            serializer = self.get_serializer(dish)
            return Response({"status": 1, "data": serializer.data})
        except Dish.DoesNotExist:
            return Response({"status": 0,
                             "error": "invalid id"})



# class AddKitchen(generics.GenericAPIView):

#     serializer_class = AddKitchenSerializer()


