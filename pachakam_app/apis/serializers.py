from rest_framework import serializers
from .models import *


class categoryListSerilizers(serializers.ModelSerializer):

    """Model serializer for listing cateogories"""

    class Meta:
        model = Category
        fields = "__all__"


class DishlistSerializer(serializers.ModelSerializer):
    """
    Model serialiser for listing all the dishes
    """

    class Meta:
        model = Dish
        fields = "__all__"


class IngridientListSerialiser(serializers.ModelSerializer):
    """
    Model serializer for the ingridient list
    """

    class Meta:
        model = IngridientList
        fields = "__all__"


class DishDetialsSerializer(serializers.ModelSerializer):
    """
        Model serializer for detailed view for the dishes
    """

    ingridients_list = serializers.SerializerMethodField()

    class Meta:
        model = Dish
        fields = ("id", "name", "total_time", "type",
                  "category", "ingridients_list")

    def get_ingridients_list(self, obj):
        try:
            ingridients_list = IngridientList.objects.filter(dish=obj)
            serializer = IngridientListSerialiser(ingridients_list, many=True)
            return serializer.data
        except IngridientList.DoesNotExist:
            return []


class categoryDetailedSerialiser(serializers.ModelSerializer):
    """
        Model Serialiser for category 
    """

    class Meta:
        model = Category
        fields = "__all__"
