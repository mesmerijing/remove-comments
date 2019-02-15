
import re
 
input_file=input("Give a text file:")
with open (input_file,"r") as f:
     data= f.read()
data = re.sub(r'\n#.*', "",data)
with open(input_file,"w") as f:
     f.write(data)
