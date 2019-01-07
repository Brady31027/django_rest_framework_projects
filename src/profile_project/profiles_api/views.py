from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializer

# Create your views here.
class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Use HTTP methods as function(get, post, patch, put, delete)',
            'Similar to traditional Django View',
            'Gives most control of your app logic',
            'It\'s mapped manually to URLs',
        ]
        return Response({'message': 'Hello!',
                         'an_apiview': an_apiview})

    def post(self, request):
        serializerObj = serializer.HelloSerializer(data=request.data)
        if serializerObj.is_valid():
            name = serializerObj.data.get('name')
            msg = 'Hello {0}'.format(name)
            return Response({'message':msg})
        else:
            return Response(serializerObj.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        return Response({'method': 'patch'})

    def delete(self, request):
        return Response({'method': 'delete'})
