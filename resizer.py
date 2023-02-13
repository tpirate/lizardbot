from PIL import Image
import os
import PIL
import glob

old = [1600, 900]
new = [1024, 768]

def resize(file):
    image = Image.open(file)
    x = round(new[0]*image.size[0]/old[0])
    y = round(new[1]*image.size[1]/old[1])
    resized_image = image.resize((x,y))
    resized_image.save(file, optimize=True, quality=75)

if __name__ == "__main__":
    for i in range(11):
        resize('templates/champ/temchamp' + str(i) + '.png')