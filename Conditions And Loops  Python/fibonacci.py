# It is used to find nth fibonacci number

n=int(input("enter a number"))
def fibonacci_seq(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for _ in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")

fibonacci_seq(n)
