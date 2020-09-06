n=int(input())
arr=list(map(int,input().split()))
val=int(input())
def binary_search(arr,val):
    start=0
    end=n-1
    while start<=end:
    	mid=(start+end)//2
    	if arr[mid]>val:
        	end=mid-1
    	elif arr[mid]<val:
        	start=mid+1
    	elif arr[mid]==val:
        	return mid
    return -1

print(binary_search(arr,val))
    
