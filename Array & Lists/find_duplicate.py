n=int(input())
k=[int(x) for x in input().split()]
p=0
for i in k:
    p=p+1
    for j in k[p:]:
        if i==j:
            print(i)
