from django.urls import path
from . import views

urlpatterns = [
    path('complete-hero-name', views.complete_hero_name),
    path('complete-item-name', views.complete_item_name),
    path('upload-heroes', views.upload_heroes),
]