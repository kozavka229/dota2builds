from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_build, name="create-build"),
    path('edit/<int:pk>', views.edit_build, name="edit-build"),
    path('heroes/<int:hero_pk>', views.get_hero_builds, name="hero-builds"),
    path('heroes/<slug:hero_slug>', views.get_hero_builds),
    path('api/', include('dota2builds_api.urls'))
]
