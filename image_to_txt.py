import cv2
image, txt = input("Image: "), input("Destination TXT: ")
open(txt, "w").close()
with open(txt, "a") as file:
    for row in cv2.imread(image):
        for pixel in row:
            n = sum(pixel) // 3
            if 0 <= n < 26: file.write("M ")
            elif 26 <= n < 51: file.write("# ")
            elif 51 <= n < 76: file.write("Q ")
            elif 76 <= n < 102: file.write("A ")
            elif 102 <= n < 128: file.write("& ")
            elif 128 <= n < 153: file.write("0 ")
            elif 153 <= n < 178: file.write("+ ")
            elif 178 <= n < 204: file.write("- ")
            elif 204 <= n < 230: file.write(". ")
            elif 230 <= n < 256: file.write("  ")
        file.write("\n")