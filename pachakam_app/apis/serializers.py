from rest_framework import serializers
from .models import *


# # class categoryListSerilizers(serializers.ModelSerializer):

# #     """
# #         Model serializer for listing cateogories
# #     """

# #     class Meta:
# #         model = Category
# #         fields = "__all__"


class DishlistSerializer(serializers.ModelSerializer):

    """
        Model serialiser for listing all the dishes
    """

    class Meta:
        model = Dish
        fields = "__all__"

# # class IngridientNameSerialiser(serializers.ModelSerializer):
    
# #     """
# #         Model serializer for getting the name of the 
# #         ingridient for the dishes
# #     """

# #     class Meta:
# #         model = Ingridient
# #         fields = ("name",)

# # class MeasurmentNameSerialiser(serializers.ModelSerializer):

# #     """
# #         Model serialiser for getting the name of the measurment unit
# #     """

# #     class Meta:
# #         model = Unit
# #         fields = ("name",)


 
class IngridientListSerialiser(serializers.ModelSerializer):
    
    """
    Model serializer for the ingridient list
    """
    class Meta:
        model = Ingridient
        fields = "__all__"


class StepIdSerialiser(serializers.ModelSerializer):
    
    """
        Model Serialiser of returning the step id of the selected dish
    """
    class Meta:
        model = step
        fields = "__all__"


# class StepDetailedSerialiser(serializers.ModelSerializer):
    
#     """
#         Model serializer for detailed steps
#     """
#     class Meta:
#         model = step
#         fields = "__all__"


class DishDetialsSerializer(serializers.ModelSerializer):
    
    """
        Model serializer for detailed view for the dishes
    """

    ingridients_list = serializers.SerializerMethodField()
    steps = serializers.SerializerMethodField()

    class Meta:
        model = Dish
        fields = "__all__"

    def get_ingridients_list(self, obj):
        
        """
            Method for returning the ingridient list
        """
        
        try:
            ingridients_list = Ingridient.objects.filter(dish=obj)
            serializer = IngridientListSerialiser(ingridients_list, many=True)
            return serializer.data
        except IngridientList.DoesNotExist:
            return []

    def get_steps(self, obj):

        """
            Method for returning the step ids of the current step
        """

        try:
            steps = step.objects.filter(dish=obj)
            serializer = StepIdSerialiser(steps, many=True)
            return serializer.data
        except step.DoesNotExist:
            return []



# # class categoryDetailedSerialiser(serializers.ModelSerializer):
    
# #     """
# #         Model Serialiser for category 
# #     """

# #     class Meta:
# #         model = Category
# #         fields = "__all__"
