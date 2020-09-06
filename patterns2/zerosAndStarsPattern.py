if n == 4

*000*000*
0*00*00*0
00*0*0*00
000***000

n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        if i==j:
            print('*',end='')
        else:
            print('0',end='')
        j=j+1
    k=n-i
    while k>=1:
        print('0',end='')
        k=k-1
    x=1
    while x<=(n-i+2):
        if x==1 or x==(n-i+2):
            print('*',end='')
        else:
            print('0',end='')
        x=x+1
    s=i-1
    while s>=1:
        print('0',end='')
        s=s-1
    print()
    i=i+1
        
