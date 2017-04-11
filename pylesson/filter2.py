from PIL import Image
from random import randint

img = Image.open("unnamed.png")
pixels = img.load()

x, y = img.size

for i in range(x):
    for j in range(y):
        r, g, b, a = pixels[i, j]
        # pixels[i, j] = randint(0,255), g, b, a
        pixels[i, j] = r + randint(-20,20), g + randint(-20,20), b + randint(-20,20), a



img.save("unnamed5.png")
img.show()
