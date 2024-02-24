from PIL import Image
import numpy as np


def stringrep(filename):
    image = Image.open(filename)

    image = image.convert("1")

    width, height = image.size

    # width = width / 10
    # height = height / 10

    string_representation = ""
    for i in range(int(height)):
        for j in range(int(width)):
            if image.getpixel((j, i)) == 0:
                string_representation += " "
            # if image.getpixel((j, i)) >= 200:
            # asciiCanvas[i][j] = "."
            else:
                string_representation += "."
            # J is not possibly unbound moron
            # there's no boundary you don't know that because you have a retarded
            # implementation of arrays python
        string_representation += "\n"

    return string_representation


#
# with open("pixelinfo.txt", "w") as file:
#     for y in range(height):
#         for x in range(width):
#             pixel_value = image.getpixel((x, y))
#             file.write(f"Pixel at ({x}, {y}: {pixel_value})")
"""
stringrep = ""
for row in asciiCanvas:
    for item in row:
        stringrep += str(item)
    stringrep += "\n"

"""


def imgtonp(filename):
    im = Image.open(filename)
    width, height = im.size
    im = im.convert("1")
    a = np.asarray(im)

    return a, width, height


def writeTofile(string_representation):
    with open("asciifile.txt", "w") as file:
        file.write(string_representation)


def main():
    print(stringrep("./butterfly.jpg"))


if __name__ == "__main__":
    main()


"""
##########################################################################
#### This is part of the code where i store random things for later ######
##########################################################################

narr, width, height = imgtonp("./lilly.png")
    np.set_printoptions(threshold=np.inf)
    print(narr)

"""
