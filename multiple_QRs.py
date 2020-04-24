import sys,qrtools
from PIL import Image
import os
im = Image.open("answer.jpg")
width, height = im.size
#print(width)
#print(height)
result = ""
for a in (0,1,2,3,4):
     for b in (0,1,2,3):
          top = height / 5 * a
          left = width / 4 * b
          right = width / 4 * (b+1)
          bottom = height / 5 * (a+1)
          im1 = im.crop((left, top, right, bottom))   
          im1.save("answer" + str(a) + str(b) + ".jpg")

          qr = qrtools.QR()
          qr.decode("answer" + str(a) + str(b) + ".jpg")
          mydata = qr.data
          x = mydata.encode('utf-8')
          #x = x.split()
          result = result + " " + x
          #print(x)
          os.remove("answer" + str(a) + str(b) + ".jpg")
          print(result)
