def pushZeroToEnd(arr):
    c=[]
    i=0
    j=0
    for i in range(n):
        if arr[i]!=0:
            c.append(arr[i])
            j=j+1
    while j<n:
        c.append(0)
        j=j+1
    return c
    
n=int(input())
arr=list(map(int,input().split()))

for i in pushZeroToEnd(arr):
    print(i,end=' ')
