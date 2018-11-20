from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Company, Profile, Position, Department


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class CompanySerializers(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name')


class DepartmentSerializers(serializers.ModelSerializer):

    supervisor = UserSerializers()
    workers = UserSerializers(many = True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'supervisor', 'workers')



class PositionSerizlizers(serializers.ModelSerializer):

    company = CompanySerializers()

    class Meta:
        model = Position
        fields = ('id', 'name', 'company')


class ProfileSerializers(serializers.ModelSerializer):

    user = UserSerializers()
    position = PositionSerizlizers(many = True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'name', 'last_name', 'phone', 'email', 'position')