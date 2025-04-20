import os
from django.utils.text import slugify

images_path = "./dota2site/dota2builds/static/images/items"
items_path = "./out.txt"

with open(items_path) as f:
    items_dict = dict((slugify(n.strip()), n.strip()) for n in f.read().split("\n"))

items = set(items_dict.keys())
images = set((n.replace("-item.png", "") for n in os.listdir(images_path)))

print("\n".join(items.difference(images)))
print("\n".join(images.difference(items)))
print(f"{len(items)=}")
print(f"{len(images)=}")

