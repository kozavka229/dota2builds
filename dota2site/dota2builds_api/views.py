from typing import Type

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models

from dota2builds.models import Hero, Item


@api_view(["POST"])
def complete_hero_name(request):
    return complete_name(request.POST, Hero)


@api_view(["POST"])
def complete_item_name(request):
    return complete_name(request.POST, Item)


@api_view(["POST"])
def upload_heroes(request):
    try:
        uploaded_file = request.FILES['file']
    except KeyError:
        return Response({"error": "no file"})

    if request.POST.get("clear") == 1:
        Hero.objects.all().delete()

    try:
        content = uploaded_file.read().decode('utf-8')
        for line in content.split('\r\n'):
            if Hero.objects.filter(name=line).exists():
                continue
            hero = Hero.objects.create(name=line)
            hero.save()
    except Exception as e:
        return Response({f"Ошибка: {e}"}, status=500)
    else:
        return Response({"result": "Loaded " + ", ".join(content.split('\r\n'))})


def complete_name(params: dict, model_cls: Type[models.Model]):
    try:
        text = params["text"]
    except KeyError:
        return Response({"error": f"request no has 'text' : {params}"}, status=500)
    else:
        objs = model_cls.objects.filter(name__startswith=text)
        return Response({"result": ",".join(map(lambda e: e.name, objs))})
