Pattern for N = 4

4444444
4333334
4322234
4321234
4322234
4333334  
4444444

n=int(input())
for i in range(1,n+1,1):
    for num1 in range(n,n-i,-1):
        print(num1,end='')
    for num2 in range(n-i):
        print(n-i+1,end='')
    for num3 in range(n-i):
        print(n-i+1,end='')
    for num4 in range(n-i+2,n+1,1):
        print(num4,end='')
    print()
for i in range(1,n,1):
    for num5 in range(n,i,-1):
        print(num5,end='')
    for num6 in range(i):
        print(i+1,end='')
    for num7 in range(i):
        print(i+1,end='')
    for num8 in range(i+2,n+1):
        print(num8,end='')
    print()
