if n == 5 then

  *
 ***
*****
 ***
  *
  
n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    p=i
    while j<=i:
        print(p,end='')
        j=j+1
        p=p+1
    k=2*(i-1)
    x=i-1
    while x>=1 :
        print(k,end='')
        k=k-1
        x=x-1
    print()
    i=i+1
        
