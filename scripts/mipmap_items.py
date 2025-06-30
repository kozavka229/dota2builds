import os
from PIL import Image

# Директория с изображениями
IMAGES_DIR = 'D:/Python/dota2builds/upload/items'

# Размер изображения (width x height)
TILE_WIDTH = 40
TILE_HEIGHT = 30

# Путь для сохранения результирующего изображения и CSS-файла
SPRITE_OUTPUT_PATH = '../dota2site/dota2builds/static/images/minimap/minimap_item_sheet.png'
CSS_OUTPUT_PATH = '../dota2site/dota2builds/static/css/dota2minimapitems.css'

# Список разрешённых форматов изображений
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']

def load_images(directory):
    images = {}
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                full_path = os.path.join(root, filename)
                im = Image.open(full_path)
                im = im.resize((TILE_WIDTH, TILE_HEIGHT))  # Масштабируем до 40x30
                images[filename[:-len(ext)].lower()] = im
    return images

def generate_sprite(images):
    num_cols = len(images.keys())
    sprite_width = num_cols * TILE_WIDTH
    sprite_height = TILE_HEIGHT
    sprite = Image.new('RGBA', (sprite_width, sprite_height))

    x_offset = 0
    y_offset = 0
    for filename, img in images.items():
        sprite.paste(img, (x_offset, y_offset))
        x_offset += TILE_WIDTH
    return sprite

def write_css_classes(images):
    with open(CSS_OUTPUT_PATH, 'w') as css_file:
        css_file.write(".d2mi {\n")
        css_file.write("\tbackground-image: url('%s');\n" % SPRITE_OUTPUT_PATH.replace("dota2site/dota2builds", ""))
        css_file.write("\tbackground-repeat: no-repeat;\n")
        css_file.write("\tdisplay: inline-block;\n")
        css_file.write("\twidth: %spx;\n" % TILE_WIDTH)
        css_file.write("\theight: %spx;\n" % TILE_HEIGHT)
        css_file.write("}\n\n")

        for idx, filename in enumerate(sorted(images.keys())):
            pos_x = -(idx * TILE_WIDTH)
            css_file.write(".d2mi.%s {\n" % filename.replace('-item','').lower())
            css_file.write("\tbackground-position: %spx %spx;\n" % (pos_x, 0))
            css_file.write("}\n\n")

def main():
    images = load_images(IMAGES_DIR)
    sprite = generate_sprite(images)
    sprite.save(SPRITE_OUTPUT_PATH)
    write_css_classes(images)
    print(f"Спрайт сохранён в {SPRITE_OUTPUT_PATH}, CSS-файл сохранён в {CSS_OUTPUT_PATH}")

if __name__ == "__main__":
    main()