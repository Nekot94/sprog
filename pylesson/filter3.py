from PIL import Image
from random import randint

img = Image.open("unnamed.png")
pixels = img.load()

x, y = img.size

while True:
    try:
        dep = int(input("введите глубину сепии: "))
        break
    except ValueError:
        print("Введи число я сказал!!!")


for i in range(x):
    for j in range(y):
        r, g, b, a = pixels[i, j]
        mid = (r + g + b) // 3
        pixels[i, j] = mid + dep * 2, mid + dep, mid, a



img.save("unnamed6.png")
img.show()
