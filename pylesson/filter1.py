from PIL import Image

img = Image.open("unnamed.png")
pixels = img.load()

x, y = img.size

for i in range(x):
    for j in range(y):
        r, g, b, a = pixels[i, j]
        pixels[i, j] = r * 2, g * 2, b * 2, a


img.save("unnamed3.png")
img.show()
