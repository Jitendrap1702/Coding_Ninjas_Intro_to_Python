num=int(input())
k=len(str(num))
s=0
for i in str(num):
    s=s+(int(i)**k)
    
if int(s)==num:
    print('true')
else:
    print('false')
