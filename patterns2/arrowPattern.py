if n == 11:

*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*

n=int(input())
n1=(n+1)//2
i=1
while i<=n1:
    spaces1=1
    while spaces1<=i-1:
        print(' ',end='')
        spaces1=spaces1+1
    stars1=1
    while stars1<=i:
        print('* ',end='')
        stars1=stars1+1
    print()
    i=i+1
n2=n//2
j=1
while j<=n2:
    spaces2=1
    while spaces2<=n2-j:
        print('* ',end='')
        stars2=stars2+1
    print()
    j=j+1
            
    
        print(' ',end='')
        spaces2=spaces2+1
    stars2=1
    while stars2<=n2-j+1:
    
