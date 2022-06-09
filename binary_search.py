#binary search using recursion
#defining the function
def BS(arr,lower,upper,s):
	if upper>=lower:
		mid=(upper+lower)//2
		#if element is present in the middle
		if arr[mid]==s:
			return mid
		#if element is less than middle element
		elif arr[mid]>s:
			return BS(arr,lower,mid-1,s)
		#if element is greater than middle element
		else:
			return BS(arr,mid+1,upper,s)
	else:
		return -1

n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
	a=int(input("Enter the number:"))
	arr.append(a)
arr=sorted(arr)
print(arr)
s=int(input("Enter the number you want to search:"))

#Calling the function
res=BS(arr,0,n-1,s)
if res!=(-1):
	print("Entered number is present in index %d" %res)
else:
	print("Entered number is not present")
