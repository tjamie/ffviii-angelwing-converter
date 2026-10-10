import os
from pkg.convert_images import convert_images

if __name__ == "__main__":
    # Path to Project Angelwing field background textures
    raw_path: str = r"D:\SteamLibrary\steamapps\common\FINAL FANTASY VIII Remastered\DEMASTER_EXP\textures\field_bg"
    path = os.path.abspath(raw_path)
    convert_images(path)