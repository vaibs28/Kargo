import sys

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
		if str2[i] in dict.values():
			print("false")
			exit()
		else:
			dict[str1[i]] = str2[i]
print("true");

