import os
i=0
for file in os.listdir("./"):
	os.rename(file,str[i]+".png")
	i+=1
