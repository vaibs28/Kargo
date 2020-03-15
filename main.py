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

dict = {}								#dictionary to store the mapping
for i in range(len(str1)):				#iterate through all the characters in the strings
	if str1[i] in dict:					#if character is in the dictionary
		if(dict[str1[i]]!=str2[i]):		#checks if the character has already been mapped with the current str2 character, if no then prints false and terminates
			print("false")
			exit()
	else:
		dict[str1[i]] = str2[i]			#add the mapping to dictionary
print("true")							#print true if all the characters can be mapped as per the conditions