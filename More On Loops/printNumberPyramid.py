For eg. N = 6
123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456

n=int(input())
for i in range(1,n+1,1):
    for s1 in range(i-1):
        print(' ',end='')
    for num1 in range(i,n+1,1):
        print(num1,end='')
    print()
for j in range(1,n,1):
    for s2 in range(1,n-j):
        print(' ',end='')
    for num2 in range(n-j,n+1,1):
        print(num2,end='')
    print()
