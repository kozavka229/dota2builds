from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Hero(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Имя героя")
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Hero, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Build(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, verbose_name="Герой")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Создатель")

    def __str__(self):
        return f'Build for {self.hero} "{self.name}" by {self.owner}'


class BuildItemInfo(models.Model):
    build = models.ForeignKey(Build, related_name="itemsinfo", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()
    description = models.TextField(max_length=300, blank=True)

    class Meta:
        unique_together = ('build', 'item')
        ordering = ('order', )

