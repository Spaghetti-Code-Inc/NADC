import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import colorsys

def find_max_and_min(file):
    max = -1000
    min = 1000
    with open(file, 'r') as r:
        for i in r.readlines():
            for j in i.split(','):
                each = float(j)
                if(each > max): max = each
                elif(each < min): min = each

    print(f"Min: {min}, Max: {max}")
    return [max, min]

def make_map_black_white(file, out_name, invert):
    # Returns max and min vals of the file: [max, min]
    vals = find_max_and_min(file)

    difference = vals[0]-vals[1]
    img = []

    with open(file, 'r') as r:
        for i, line in enumerate(r.readlines()):
            img.append([])
            
            if(line[-1] == '\n'): 
                line = line[0:-1]

            for each in line.split(','):
                height = float(each)
                  
                # hsv
                # 5/6 because we only want to use that part of the color scale
                # height = (height-min)/maxCheck*10/12
                # img[i].append([height, .99, .99])
                
                # Height is transformed to a percentage from the minimum value to the maximum value
                if(invert):
                    height = (difference-height+vals[1])/difference
                else:
                    height = (height-vals[1])/difference

                
                # Puts height on the correct 0-255 scale
                # rounding to 3 decimal places makes calculation faster and does not affect the color outcome
                height = 255*round(height, 3)

                img[i].append([height, height, height]) # black->white
                
                # if(height < d):img[i].append([0, 0, 3*height])
                # elif (height < 2*d): img[i].append([0, 3*(height-d), d*3])
                # else: img[i].append([3*(height-2*d), d*3,d*3])

    im = Image.fromarray(np.uint8(img))

    im.save(out_name + '.png')

def make_map_from_hsv(file, out_name, invert):
    # Returns max and min vals of the file: [max, min]
    vals = find_max_and_min(file)

    difference = vals[0]-vals[1]
    img = []

    with open(file, 'r') as r:
        print('logging data')
        for i, line in enumerate(r.readlines()):
            img.append([])
            
            if(line[-1] == '\n'): 
                line = line[0:-1]

            for each in line.split(','):
                height = round(float(each), 4)
                  
                # height is on scale from [0, 470] first and last 100 affect the other 2 variables
                if(invert):
                    height = int((difference-height+vals[1])/difference*470)
                else:
                    height = int((height-vals[1])/difference*470)


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
                img[i].append(save)
    print('saving image')
    im = Image.fromarray(np.uint8(img))
    im.save(out_name + '.png')

# find_max_and_min('FY23_ADC_Slope_PeakNearShackleton.csv')
make_map_from_hsv("FY23_ADC_Slope_PeakNearShackleton.csv", 'Slope4', False)