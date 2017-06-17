# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class ListCategories(generics.GenericAPIView):

    """
        View for listing all the categories of the 
        food item
    """

    serializer_class = categoryListSerilizers

    def get(self, request, *args, **kwargs):
        """
            Get method for the list view
        """
        categories = Category.objects.all()
        serializer = self.get_serializer(categories, many=True)
        return Response({"status": "ok",
                         "data": serializer.data})


class CategoryDetailed(generics.GenericAPIView):

    """
        View for getting the detailed data of the category selected
    """

    serializer_class = categoryDetailedSerialiser

    def get(self, request, *args, **kwargs):

        """
            Get method for the category
        """

        category_id = self.kwargs.get("category_pk")
        category = Category.objects.filter(id=category_id)
        if len(category) > 0:
            serializer = self.get_serializer(category[0])
            return Response({"status": "ok", "data": serializer.data})
        else:
            return Response({"status": "No such category exist", "data": []})


class ListDishes(generics.GenericAPIView):

    """
        View for listing all the dishes under current catgories
    """

    serializer_class = DishlistSerializer

    def get(self,request, *args, **kwargs):

        """
            Get method for list dihes
        """

        category_id = self.kwargs.get('category_pk')
        dishes = Dish.objects.filter(category__id=category_id)
        page_num = request.GET.get('page', 1)
        paginator = Paginator(dishes, 1)
        try:
            paginated_entries = paginator.page(int(page_num))
        except PageNotAnInteger as e:
            paginated_entries = paginator.page(1)
        except EmptyPage:
            paginated_entries = paginator.page(paginator.num_pages)
        serializer = self.get_serializer(paginated_entries, many=True)
        if len(dishes) > 0:
            if int(page_num) < paginator.num_pages:
                load_more_required = True
            else:
                load_more_required = False
            return Response({"status": "ok", "data": serializer.data,
                             "load_more_required": load_more_required})
        else:
            return Response({"status": "No dishes in this category",
                             "data": []})

class DishDetails(generics.GenericAPIView):

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
            category_id = self.kwargs.get('category_pk')
            dish = Dish.objects.get(id=dish_id)
            serializer = self.get_serializer(dish)
            if int(category_id) != dish.category_id:
                return Response({"status": "Dish with this id doesnot exist",
                             "data": []})
            return Response({"status": "ok", "data": serializer.data})
        except Dish.DoesNotExist:
            return Response({"status": "Dish with this id doesnot exist",
                             "data": []})


class StepDetails(generics.GenericAPIView):

    """
        View for getting the step details
    """

    serializer_class = StepDetailedSerialiser

    def get(self, request, *args, **kwargs):

        """
            get method for the view
        """

        try:
            step_id = self.kwargs.get("step_id")
            steps = step.objects.get(id=step_id)
            serializer = self.get_serializer(steps)
            return Response({"status": "ok", "data": serializer.data})
        except step.DoesNotExist:
            return Response({"status": "Step with this id exists","data":[]})

