from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_build),
    path('<slug:hero_slug>', views.get_hero_builds),
    path('api/', include('dota2builds_api.urls'))
]
