def sort012(arr,n):
    low=0
    mid=0
    high=n-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low=low+1
            mid=mid+1

        elif arr[mid]==1:
            mid=mid+1

        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high=high-1

n=int(input())
arr=list(map(int,input().split()))

sort012(arr,n)

for i in arr:
    print(i,end=' ')
