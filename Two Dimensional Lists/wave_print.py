def wavePrint(arr):
    for i in range(n):
        if i%2==0:
            for j in range(m):
                print(arr[j][i],end=' ')
        
        else:
            for j in range(m-1,-1,-1):
                print(arr[j][i],end=' ')

#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
# arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
arr = []
for i in range(m):
    lst1 = [int(x) for x in input().strip().split(' ')]
    arr.append(lst1)
wavePrint(arr)
