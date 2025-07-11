from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from loguru import logger

from .forms import BuildForm, BuildItemOrderFormSet
from .models import Build, Hero, Item


def profile(request, user_pk: int = None):
    user = request.user if user_pk is None else get_object_or_404(get_user_model(), pk=user_pk)
    return render(request, 'profile.html', context={
        'target': user,
        'builds': Build.objects.filter(owner_id=user)
    })


def index(request):
    return render(request, 'index.html', context={'heroes': Hero.objects.all()})


def get_hero_builds(request, hero_slug: str = None, hero_pk: int = None):
    hero: Hero
    if hero_slug is not None:
        hero = get_object_or_404(Hero, slug=hero_slug)
    elif hero_pk is not None:
        hero = get_object_or_404(Hero, pk=hero_pk)
    else:
        return redirect("index")

    builds = Build.objects.filter(hero=hero)
    return render(request, 'hero-builds.html', context={'hero': hero, 'builds': builds})


@login_required
def build_editor(request, build_pk: int = None):
    build: Build | None
    if build_pk is not None:
        build = get_object_or_404(Build, pk=build_pk)
        if build.owner != request.user:
            return HttpResponseForbidden(request)
    else:
        build = None

    build_form = BuildForm(request.GET if build is None else None, instance=build)
    build_formset = BuildItemOrderFormSet(instance=build)

    if request.method == "POST":
        build_form = BuildForm(request.POST, instance=build)
        if build_form.is_valid():
            if build_form.cleaned_data.get('delete'):
                if build is not None:
                    build.delete()
                return redirect("hero-builds", hero_pk=build_form.cleaned_data['hero'].pk)

            build = build_form.save(commit=False)
            build.owner = request.user

            build_formset = BuildItemOrderFormSet(request.POST, instance=build)
            if build_formset.is_valid():
                build_form.save()

                for idx, oform in enumerate(build_formset.ordered_forms):
                    oform.instance.order = idx
                    oform.instance.save()

                build_formset.save()
                return redirect("build-info", build_pk=build.pk)

    return render(request, 'build-editor.html', {
        "form": build_form,
        "formset": build_formset,
        "items": Item.objects.all()
    })


def build_info(request, build_pk: int):
    build: Build = get_object_or_404(Build, pk=build_pk)
    return render(request, "build-info.html", context={
        "build": build
    })
