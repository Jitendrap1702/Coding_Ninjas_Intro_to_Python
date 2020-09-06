def rowWiseSum(arr):
    rowSum=[]
    for i in range(m):
        sum=0
        for j in range(n):
            sum=sum+arr[i][j]
        rowSum.append(sum)
    
    return rowSum


#Main
m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
l=rowWiseSum(arr)
print(*l)
