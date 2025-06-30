from django.db import models
from django.utils.text import slugify


class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to="upload/items", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        if not self.image:
            self.image = f"{self._meta.get_field("image").upload_to}/{self.slug}-item.png"

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

    def __str__(self):
        return f"Build for {self.hero} \"{self.name}\""


class BuildItemInfo(models.Model):
    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()
    description = models.TextField(max_length=300, blank=True)

    class Meta:
        ordering = ('order', )

