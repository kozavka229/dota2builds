from django.db import models
from django.utils.text import slugify


class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image_name = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.image_name:
            self.image_name = slugify(self.name) + '-item'
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ItemDescription(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"Item description for {self.item}"


class Hero(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Hero, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Build(models.Model):
    name = models.CharField(max_length=30)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through="BuildItemOrder")

    def __str__(self):
        return f"Build for {self.hero} \"{self.name}\""


class BuildItemOrder(models.Model):
    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']
