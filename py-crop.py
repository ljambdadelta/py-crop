from os import path, listdir
from PIL import Image

source_dir = "W:\\Downloads\\Test\\Src\\"
dest_dir = "W:\\Downloads\\Test\\Dst\\"

for file in filter(lambda f: ".png" in f, listdir(source_dir)):
    with Image.open(path.join(source_dir, file)) as im:
        (left_1, upper_1, right_1, lower_1) = (0, 90, 2880, 1800)
        im_crop_first = im.crop((left_1, upper_1, right_1, lower_1))
        
        (left_2, upper_2, right_2, lower_2) = (0, 0, 2880, 1620)
        im_crop_last = im_crop_first.crop((left_2, upper_2, right_2, lower_2))
        
        im_crop_last.save(path.join(dest_dir, file))
