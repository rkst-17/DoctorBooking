from django.urls import path
from backend import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
