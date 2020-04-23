#Napisz program
import sys,qrtools
from sympy import isprime
doCompare = False
if(len(sys.argv) > 1):
     if(sys.argv[1] != 0):
          filename = sys.argv[1]
          if(len(sys.argv) == 3):
               if(sys.argv[2] != 0):
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
                         for word in x:
                              if(splitedline[0] == word):
                                   print(splitedline[0])
                                   print("good result")

                    
     file.close()
     print (result + "]")
