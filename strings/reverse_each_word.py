def reverseword(s):
    str2=[]
    for str in s.split():
        str2.append(str[::-1])
    return str2

s=input()

k=reverseword(s)

for i in k:
    print(i,end=' ')
        
