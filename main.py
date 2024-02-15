from PIL import Image

image = Image.open("./lilly.png")

image = image.convert("L")


width, height = image.size
string_representation = ""

asciiCanvas: "list" = [["" * width for _ in range(height)]]
for i in range(height):
    for j in range(width):
        if image.getpixel((j, i)) == 0:
            continue
        # if image.getpixel((j, i)) >= 200:
        # asciiCanvas[i][j] = "."
        string_representation += "."
        # J is not possibly unbound moron
        # there's no boundary you don't know that because you have a retarded
        # implementation of arrays python
    string_representation += "\n"

with open("pixelinfo.txt", "w") as file:
    for y in range(height):
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            file.write(f"Pixel at ({x}, {y}: {pixel_value})")
"""
stringrep = ""
for row in asciiCanvas:
    for item in row:
        stringrep += str(item)
    stringrep += "\n"

"""
with open("asciifile.txt", "w") as file:
    file.write(string_representation)
