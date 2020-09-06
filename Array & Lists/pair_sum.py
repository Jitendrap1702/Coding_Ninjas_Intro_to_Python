n=int(input())
l=list(map(int,input().split()))
x=int(input())
k=0
for i in l:
    k=k+1
    for j in l[k:]:
        if (j+i)==x:
            print(min(i,j),' ',max(i,j))
        else:
            continue
    
