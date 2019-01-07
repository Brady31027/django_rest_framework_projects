from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

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
