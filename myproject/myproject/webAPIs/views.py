from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Movies, Collection
from . serializers import movieSerializer, collectionSerializer


### class view for movies list
class movieslist(APIView):

    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            movie = Movies.objects.get(id=id)
            serializer = movieSerializer(movie)
            return Response(serializer.data)
        movie = Movies.objects.all()
        serializer = movieSerializer(movie, many = True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = movieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id1 = pk
        movie = Movies.objects.get(id=id1)
        serializer = movieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id1 = pk
        obj = Movies.objects.get(id=id1)
        obj.delete()
        return Response({'msg':'Data Deleted'})    


### class view for collection list       
class collectionlist(APIView):
    
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            movie = Collection.objects.get(id=id)
            serializer = collectionSerializer(movie)
            return Response(serializer.data)
        movie = Collection.objects.all()
        serializer = collectionSerializer(movie, many = True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = collectionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        # id1 = pk
        movie = Collection.objects.get(id=pk)
        serializer = collectionSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # id1 = pk
        obj = Collection.objects.get(id=pk)
        obj.delete()
        return Response({'msg':'Data Deleted'}) 