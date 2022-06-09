#program to find compound interest using function
def CI(P,n,r):
	ci=P*(pow((1+r/100),n))
	return ci
P=float(input("Enter the Principle amount:"))
r=float(input("Enter the rate:"))
t=float(input("Enter the number of years:"))
#function call
ci=CI(P,t,r)
print("The compound interest is %.2f" %ci)

