#program to find factorial of a number using recursion
a=int(input("Enter the number:"))
def factorial(n):
	if n==0:
		return fact
	else:
		return n*factorial(n-1)	
fact=1
res=factorial(a)
print("Factorial of given number is", res)
