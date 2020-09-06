n=int(input())
if n==0:
    pass
else:
	l=list(map(int,input().split()))
def swap(l):
    if n%2==0:
        for i in range(0,n-1,2):
            l[i],l[i+1]=l[i+1],l[i]
        return l
        
	
    else:
        for i in range(0,n-1,2):
            l[i],l[i+1]=l[i+1],l[i]
        l[n-1]=l[n-1]
        return l
if n>0:
    for i in swap(l):
        print(i,end=' ')
	
