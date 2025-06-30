from django.http import HttpResponse
from loguru import logger
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BuildForm, BuildItemOrderFormSet
from .models import Build, Hero, Item


def index(request):
    return render(request, 'heroeslist.html', context={'heroes': Hero.objects.all()})


def get_hero_builds(request, hero_slug: str = None, hero_pk: int = None):
    if hero_slug is not None:
        hero = get_object_or_404(Hero, slug=hero_slug)
    elif hero_pk is not None:
        hero = get_object_or_404(Hero, pk=hero_pk)
    else:
        return redirect("index")

    builds = Build.objects.filter(hero=hero)
    return render(request, 'build.html', context={'hero': hero, 'builds': builds})


def edit_build(request, pk):
    build = get_object_or_404(Build, pk=pk)

    if request.method == "POST":
        form = BuildForm(request.POST, instance=build)
        if form.is_valid():
            form.save()

            formset = BuildItemOrderFormSet(request.POST, instance=build)
            if formset.is_valid():
                for idx, oform in enumerate(formset.ordered_forms):
                    oform.instance.order = idx
                    oform.instance.save()
                formset.save()

                return redirect("hero-builds", hero_pk=form.cleaned_data['hero'].pk)

    return render(request, 'createbuild.html', {
        "form": BuildForm(instance=build),
        "formset": BuildItemOrderFormSet(instance=build),
        "items": Item.objects.all()
    })


def create_build(request):
    if request.method == "POST":
        form = BuildForm(request.POST)
        if form.is_valid():
            build = Build.objects.create(name=form.cleaned_data['name'], hero=form.cleaned_data['hero'])

            formset = BuildItemOrderFormSet(request.POST, instance=build)
            if formset.is_valid():
                for idx, oform in enumerate(formset.ordered_forms):
                    oform.instance.order = idx
                    oform.instance.save()
                formset.save()

                return redirect("hero-builds", hero_pk=form.cleaned_data['hero'].pk)

    return render(request, 'createbuild.html', {
        "form": BuildForm(),
        "formset": BuildItemOrderFormSet(),
        "items": Item.objects.all()
    })
