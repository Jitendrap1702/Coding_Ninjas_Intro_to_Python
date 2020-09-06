if n == 5 then

    1
   212
  32123
 4321234
543212345

n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    num1=1
    p=i
    while num1<=i:
        print(p,end='')
        num1=num1+1
        p=p-1
    k=i-1
    j=2
    while k>=1:
        print(j,end='')
        k=k-1
        j=j+1
    print()
    i=i+1
    
