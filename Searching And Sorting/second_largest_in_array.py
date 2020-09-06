n=int(input())
arr=list(map(int,input().split()))

def greatest2Element(arr):
    S=-1
    L=-1
    if len(list(set(arr)))> 1:
        for i in range(n):
            if arr[i]>L:
                S=L
                L=arr[i]
            elif arr[i]==L:
                continue
            elif arr[i]>S:
                S=arr[i]
    else:
        S = -2147483648
    return S

print(greatest2Element(arr))
