import sys
from cv2 import imread
from math import ceil
lst = ["M", "@", "Q", "&", "0", "#", "$", "%", "A", "+", "-", ".", " "]
image, txt, chars = input("Image: "), input("Destination TXT: "), "".join([i * ceil(255 / len(lst)) for i in lst])
open(txt, "w").close()
with open(txt, "a") as file:
    img = imread(image)
    if not img:
        print(f"Couldn't read {image}")
        sys.exit(1)
    for row in img:
        for pixel in row:
            file.write(chars[ceil(sum(pixel) / 3)])
        file.write("\n")
