Pattern for N = 4

1111
000
11
0


n=int(input())
for i in range(1,n+1):
    for j in range(n-i+1):
        if i%2==0:
            print('0',end='')
        else:
            print('1',end='')
    print()
            
    