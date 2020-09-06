def largestRowCol(arr):
    max_sum1=-1
    index_max_sum1=-1
    for i in range(m):
        sum=0
        for j in range(n):
            sum+=arr[i][j]
            if sum>max_sum1:
                max_sum1=sum
                index_max_sum1=i
    
    max_sum2=-1
    index_max_sum2=-1
    for j in range(n):
        sum=0
        for i in range(m):
            sum+=arr[i][j]
            if sum>max_sum2:
                max_sum2=sum
                index_max_sum2=j
    if max_sum1>=max_sum2:
        return ['row',index_max_sum1,max_sum1]
    return ['column',index_max_sum2,max_sum2]

#Main
m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
l=largestRowCol(arr)
print(*l)
