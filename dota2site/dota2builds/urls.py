from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('builds/<int:build_pk>', views.build_info, name="build-info"),
    path('editor', views.build_editor, name="build-editor"),
    path('editor/<int:build_pk>', views.build_editor, name="build-editor"),
    path('heroes/<int:hero_pk>', views.get_hero_builds, name="hero-builds"),
    path('heroes/<slug:hero_slug>', views.get_hero_builds, name="hero-builds"),
    path('profile', views.profile, name="user-profile"),
    path('profile/<int:user_pk>', views.profile, name="user-profile"),
]
