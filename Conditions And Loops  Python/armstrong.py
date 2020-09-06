m=int(input("enter number1"))
n=int(input("enter number2"))
for num in range(m,n+1):
    sum=0
    temp=num
    while temp>0:
        rem=temp%10
        sum+=rem**3
        temp=temp/10
    if num==sum:
        print(num)
    else:
        continue
