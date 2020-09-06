if n == 5

1        1
12      21
123    321
1234  4321
1234554321

n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    spaces1=1
    while spaces1<=n-i:
        print(' ',end='')
        spaces1=spaces1+1
    spaces2=n-i
    while spaces2>=1:
        print(' ',end='')
        spaces2=spaces2-1
    k=1
    p=i
    while k<=i:
        print(p,end='')
        p=p-1
        k=k+1
    print()
    i=i+1
    
    
