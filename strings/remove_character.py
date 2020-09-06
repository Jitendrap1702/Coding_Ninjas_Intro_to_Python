def removeCharacter(s,c):
    s2=[]
    for str in s.split():
        for char in str:
            if char==c:
                x=str.replace(char,'')
        s2.append(x)
        
    return s2

s=input()
c=input()

k=removeCharacter(s,c)

for i in k:
    print(i,end=' ')
