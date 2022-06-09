#program to check whether the given input is anagram or not
s1=input("Enter the string 1:")
s2=input("Enter the string 2:")
s1=s1.lower()
s2=s2.lower()
#compare two strings to check whether they are equal or not
if sorted(s1)==sorted(s2):
	print("It is an anagram")
else:
	print("It is not an anagram")
