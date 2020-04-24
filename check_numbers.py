#Napisz program
import sys, qrtools, os
from PIL import Image
from sympy import isprime
doCompare = False
if(len(sys.argv) > 1):
     if(sys.argv[1] != 0):
          filename = sys.argv[1]
          if(len(sys.argv) == 3):
               if(sys.argv[2] == "answer.jpg"):
                    im = Image.open("answer.jpg")
                    width, height = im.size
                    #print(width)
                    #print(height)
                    answer_result = ""
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
                              answer_result = answer_result + " " + x
                              #print(x)
                              os.remove("answer" + str(a) + str(b) + ".jpg")
                              doCompare = True

                    answer_result = answer_result.split()

               elif(sys.argv[2] != 0):
                    qr = qrtools.QR()
                    qr.decode(sys.argv[2])
                    mydata = qr.data
                    x = mydata.encode('utf-8')
                    x = x.split()
                    doCompare = True   
else:
     filename = 0
     print("No file to check. Use 'python check_numbers.py filetocheckname.txt'")
     
if(filename != 0):     
     file = open(filename, "r")
     line = file.readline()
     result = "["
     isFirstElement = True
     while( line != ''):
          i = 0
          splitedline = line.split()  
          splitedline[1] = int(splitedline[1],16)
          line = file.readline()
          if(isprime(splitedline[1])):
               if(isFirstElement):
                    result = result + splitedline[0]
                    i = i + 1
                    isFirstElement = False
                    
               else:    
                    result = result + ", " + splitedline[0]
               if(doCompare == True):
                     if(sys.argv[2] == "answer.jpg"):
                         #print("jest tu")
                         for word in answer_result:
                               if(splitedline[0] == word):
                                    print(splitedline[0])
                                    print("good result")

                     else:     
                         for word in x:
                              if(splitedline[0] == word):
                                   print(splitedline[0])
                                   print("good result")

                    
     file.close()
     print (result + "]")
