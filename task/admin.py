from django.contrib import admin
from .models import Company, Department, User, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(Department)