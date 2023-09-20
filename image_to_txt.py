import sys
from cv2 import imread
from math import ceil
lst = ["M", "@", "Q", "$", "%", "0", "+", "-", ".", " "]
image, txt, chars = input("Image: "), input("Destination TXT: "), "".join([i * ceil(255 / len(lst)) for i in lst])
open(txt, "w").close()
with open(txt, "a") as file:
    for row in imread(image):
        for pixel in row:
            file.write(chars[ceil(sum(pixel) / 3)] + " ")
        file.write("\n")
