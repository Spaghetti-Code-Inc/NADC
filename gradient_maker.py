import colorsys
from PIL import Image
import numpy as np

from easy_map_maker import find_max_and_min

def make_gradient_hsv(file):
    # Creates list of [max, min] values in the given file
    vals = find_max_and_min(file)

    img = []

    print('starting gradient')
    for i in range(470):
        height = i

        # If it is over color scale then value will be saved and decrease the saturation
        saturation = 100
        value = 100
        if(height <= 100):
            saturation = height
            height = 0
        elif(height >= 370):
            value = 100-height%370
            height = 270
        else:
            height -= 100

        # saturation drop begins 270-370: last 5/19
        rgb = colorsys.hsv_to_rgb(height/360, saturation/101, value/101)

        save = []
        save.append(round(255*rgb[0]))
        save.append(round(255*rgb[1]))
        save.append(round(255*rgb[2]))
        img.append(save)

    img = [img]
    for i in range(24):
        img.append(img[0])

    print('saving gradient')
    im = Image.fromarray(np.uint8(img))
    im.save('Gradient.png')

make_gradient_hsv(1648.68, -418.92)