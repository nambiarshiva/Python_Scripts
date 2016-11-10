from PIL import Image
k = open("filename.txt") 
c = k.read()
filename = c.split('\n')[:-1]
flag = []
for file in filename:
   print file
   im = Image.open(file) #Can be many different formats.
   pix = im.load()
   print im.size #Get the width and hight of the image for iterating over
   flag.append(chr(int(pix[3325,73])))
   flag.append(chr(int(pix[3326,73])))
   flag.append(chr(int(pix[3327,73])))

print ''.join(flag)[::-1]
