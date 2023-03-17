from rest_framework import serializers
from . models import Movies, Collection

class movieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'

class collectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'