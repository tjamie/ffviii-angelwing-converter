import os
from PIL import Image

def __manipulate_image(path: os.PathLike) -> bool:
    if path[-4:].lower() == ".png":
        img: Image = Image.open(path)
        x, y = img.size

        if x != y:
            new_img: Image = Image.new("RGBA", (x*2, y), (0, 0, 0, 0))
            new_img.paste(img, (0, 0))
            new_img.save(path, "png")
            print(f"image overwritten: {path}")
            return True        
        else:
            print(f"skipping image: {path} ({x}x{y})")

    else:
        print(f"invalid item: {path}")
    
    return False

def convert_images(path: os.PathLike):
    # path should be \DEMASTER_EXP\textures\field_bg
    # files to be converted should have resolutions such that x = 0.5,
    # final image should have resolution such that x = y

    num_conversions: int = 0

    for root, dirs, files in os.walk(path):
        for n in files:
            fp: os.PathLike = os.path.join(root, n)
            if (__manipulate_image(fp)):
                num_conversions += 1

    print(f"Process completed. {num_conversions} files converted.")