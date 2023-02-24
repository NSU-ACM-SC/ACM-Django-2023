from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
@csrf_exempt 
def home(request):
    if request.method == 'GET':
        print(request.data)
        return Response({"message":"Thank You for response."}, status=status.HTTP_200_OK)
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)