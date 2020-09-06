n=int(input())
k=[int(x) for x in input().split()]
p=0
for i in k:
    p=p+1
    if (i in k[p:]) or (i in k[:p-1]):
        continue
    else:
        print(i)
