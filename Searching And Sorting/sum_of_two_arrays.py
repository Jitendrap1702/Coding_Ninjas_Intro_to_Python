m=int(input())
A1=list(map(int,input().split()))
n=int(input())
A2=list(map(int,input().split()))

def sumOfTwoArray(m,A1,n,A2):
    carry=0
    arr=[]
    i=m-1
    j=n-1
    while i>=0 and j>=0:
        num=A1[i]+A2[j]+carry
        carry=num//10
        arr.append(num%10)
        j=j-1
        i=i-1
    while i>=0:
        num=A1[i]+carry
        carry=num//10
        arr.append(num%10)
        i=i-1
    while j>=0:
        num=A2[j]+carry
        carry=num//10
        arr.append(num%10)
        j=j-1
    arr.append(carry)
    return arr

k=sumOfTwoArray(m,A1,n,A2)
for i in k[::-1]:
    print(i,end=' ')
