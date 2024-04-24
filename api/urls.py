from django.urls import path

from api.views import Foods

urlpatterns = [
    path('foods/', Foods.as_view())
]