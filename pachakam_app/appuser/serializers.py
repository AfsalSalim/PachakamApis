from rest_framework import serializers
from .models import *



class UserSerializer(serializers.ModelSerializer):
    """
        Serializer of the user details of the author
    """

    class Meta:
        """
            Meta class for the serializer
        """
        model = AppUser
        fields = ("email", "username","id", "first_name", "last_name")



class BookListSerializer(serializers.ModelSerializer):
    """
        serializer class for listing the all the books
    """

    user = UserSerializer()

    class Meta:

        """
            Meta class for the serialiser
        """
        model = Kitchen
        # fields = ("id", "name", "like", "dislike","user", "image")
        fields = "__all__"
