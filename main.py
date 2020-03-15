import sys

#check if the proper number of arguments are passed 
if(len(sys.argv) != 3):
	print("Expecting 2 strings as command line arguments")
	exit()

#if 3 command line args are passed
str1 = sys.argv[1]
str2 = sys.argv[2]

if(len(str1)!=len(str2)):
	print("false")
	exit()

dict = {}
for i in range(len(str1)):
	if str1[i] in dict:
		if(dict[str1[i]]!=str2[i]):	
			print("false")
			exit()
	else:
		dict[str1[i]] = str2[i]
print("true")