from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API view."""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses http methods as functions (get, post, patch, put, delete',
            'it is similar to a traditional django view.',
            'Gives you the best control over the logic.',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

