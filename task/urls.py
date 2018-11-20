from django.urls import path
from .views import CompanyView, PositionView, DepartmentView, ProfileView, ProfileDetailView

urlpatterns = [
    path('company/', CompanyView.as_view(), name = 'company'),
    path('position/', PositionView.as_view(), name = 'position'),
    path('department/', DepartmentView.as_view(), name = 'department'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name = 'profile'),
]