#самодельный блюр на матрице
from  PIL import Image
from random import randrange




blmat = [[1, 2, 1],
          [2, 4, 2],
          [1, 2, 1]]
div = 16





l = len(blmat)
im = Image.open("enot.jpg")
pixels = im.load()
x, y = im.size


for i in range(x):  
    for j in range(y):
        r, g, b = pixels[i, j]
        rRes, gRes, bRes = r, g, b
        if i > l//2 and j > l//2 and i < x - l//2 and j < y - l//2:
            
            for c in range(l):
                for k in range(l):
                    rBuf, gBuf, bBuf = pixels[i - l // 2 + c, j - l // 2 + k]
                    rBuf, gBuf, bBuf= rBuf * blmat[c][k] , gBuf * blmat[c][k] , bBuf * blmat[c][k]
                    rRes  += rBuf
                    gRes  += gBuf 
                    bRes  += bBuf
            rRes = round(rRes / div)
            gRes = round(gRes / div)
            bRes = round(bRes / div)


            

        pixels[i, j] = rRes, gRes, bRes

im.save("enot.jpg")       
im.show()