from django.contrib import admin
from .models import Build, Hero, Item, BuildItemInfo


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    pass


@admin.register(Hero)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(BuildItemInfo)
class BuildItemOrder(admin.ModelAdmin):
    pass
