import os
import sys
from PIL import Image

try:
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
except Exception as err:
    print(err)
    quit()

# check whether output_folder doesn't exist
if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

for file in os.listdir(input_folder):
        path = input_folder + file
        image = Image.open(path)
        new_path = output_folder + os.path.splitext(file)[0] + ".png"
        image.save(new_path, "png")