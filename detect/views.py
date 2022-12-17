from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect
import random
import requests
import json
from firebase_admin import db

import hashlib
import pandas

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer


class RansomDetectView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UploadSerializer

    def post(self, request, format=None):

        file_uploaded = request.FILES.get('file_uploaded')

        dataset = pandas.read_csv('sha_values_ransomware.csv')
        sha_values = dataset['sha_value'].tolist()

        bytes1 = file_uploaded.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(bytes1).hexdigest()
        print(readable_hash)

        response = " "
        if readable_hash in sha_values:
            response = "Ransomware detected"
            print("Ransomware detected")

        else:
            response = "No Virus Detected"
            print("No Virus Detected")

        return Response(response)