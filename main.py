from PIL import Image
import numpy as np
from rembg import remove


# grayRamp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "
"""
grayRamp = [
    "X",
    "#",
    "%",
    "&",
    "*",
    ".",
    "~",
    "a",
    "r",
    "\\",
    "[",
    "]",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
]
"""
grayRamp = ["X", "*", " "]
rampLength = len(grayRamp)


def stringrep(image):
    # image = image.resize((600, 400))
    image = image.convert("1")

    width, height = image.size

    string_representation = ""
    for i in range(int(height)):
        for j in range(int(width)):
            if image.getpixel((j, i)) == 0:
                string_representation += "  "
            else:
                string_representation += "X0"
        string_representation += "\n"

    return string_representation


# it's a numpy array though
def npstringrep(image):
    string_representation = ""
    width, height = image.shape
    for i in range(int(height)):
        for j in range(int(width)):
            if image[i][j] > 0:
                string_representation += "X"
            else:
                string_representation += " "

            # string_representation += grayRamp[
            #     int((image[i][j]) * (rampLength - 1)) // 255
            # ]
        string_representation += "\n"

    return string_representation


def remove_background(filename):
    input = Image.open(filename)
    input = remove(input)
    return input


def reduceImage(image, window_size=(2, 2)):
    width, height = np.shape(image)
    stride_y, stride_x = window_size
    new_height = height // stride_y
    new_width = width // stride_x

    reduced_image = np.zeros((new_height, new_width), dtype=np.float32)

    for y in range(0, height, stride_y):
        for x in range(0, width, stride_x):
            window = image[y : y + stride_y, x : x + stride_x]
            average = np.mean(window)
            reduced_image[y // stride_y, x // stride_x] = average

    return reduced_image


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
    # image = remove_background("./peter.jpg")
    # print(stringrep(image))
    # image = Image.open("./peter.jpg")
    image = remove_background("./peter.jpg")
    image = image.convert("L")
    npimage = np.array(image)
    npimage = reduceImage(npimage, (5, 5))
    image = Image.fromarray(npimage)
    print(stringrep(image))


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
