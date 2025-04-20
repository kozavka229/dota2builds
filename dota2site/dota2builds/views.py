from django.shortcuts import render
from django.http import Http404

from .forms import BuildForm
from .models import Build, Hero, BuildItemOrder


def index(request):
    return render(request, 'heroeslist.html', context={'heroes': Hero.objects.all()})


def get_hero_builds(request, hero_slug: str):
    try:
        hero_slug = Hero.objects.get(slug=hero_slug)
    except Hero.DoesNotExist:
        raise Http404
    else:
        builds = Build.objects.filter(hero=hero_slug)

        return render(request, 'build.html', context={'hero': hero_slug, 'builds': builds})


def edit_build(request):
    if request.method == "POST":
        build_name = request.POST.get("build_name")
        hero = request.POST.get("hero_name")
        items = request.POST.getlist("item_list")

        if build_name and hero:
            hero = Hero.objects.filter(name=hero)
            if hero.exists():
                hero = hero.first()

                build, created = Build.objects.get_or_create(name=build_name, hero=hero)
                build.save()
                build.items.set(items)

    return render(request, 'createbuild.html', {"form": BuildForm()})


def create_build(request):
    return render(request, 'createbuild.html', {"form": BuildForm(), "formset": BuildItemOrder()})
