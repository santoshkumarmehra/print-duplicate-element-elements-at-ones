def findunique(arr,i,n):
	sum=0
	for j in range(i+1,n):
		if arr[i]==arr[j]:
			sum=arr[i]
			break
	return sum

def unique(arr,n):
	arr1=[]
	for i in range(n-1):
		result=findunique(arr,i,n)
		if result not in arr1:
			arr1.append(result)
		
	for i in arr1:
		if i != 0:
			print(i, end=" ")


arr=[3,4,2,3,4,6,3]
n=len(arr)
unique(arr,n)