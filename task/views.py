from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CompanySerializers, PositionSerizlizers, DepartmentSerializers, ProfileSerializers
from .models import Company, Profile, Position, Department

# Create your views here.
class CompanyView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializers(company, many = True)
        return Response({'data': serializer.data})


class PositionView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        position = Position.objects.all()
        serializer = PositionSerizlizers(position, many = True)
        return Response({'data': serializer.data})


class DepartmentView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        department = Department.objects.all()
        serializer = DepartmentSerializers(department, many = True)
        return Response({'data': serializer.data})


class ProfileView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializers(profile, many = True)
        return Response({'data': serializer.data})

class ProfileDetailView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        profile = Profile.objects.get(pk = pk)
        serializer = ProfileSerializers(profile)
        return Response({'data': serializer.data})