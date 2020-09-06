# It is used to find a given integer n exist in fibonacci series or not.

a=[0,1]
def checkMember(n):
    for i in range(2,700):
        a.append(a[i-1]+a[i-2])
    flag=False
    for i in range(2,700):
        if n==a[i]:
            flag=True
            break
    if flag:
        return True
    else:
        return False


n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
