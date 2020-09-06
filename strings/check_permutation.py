Total_Char=256
def checkPermutation(s1,s2):
    count=[0]*Total_Char
    
    for char in s1:
        count[ord(char)]+=1
    for char in s2:
        count[ord(char)]-=1
    
    if len(s1)!=len(s2):
        return 'false'

    for i in range(Total_Char):
        if count!=[0]*Total_Char:
            return 'false'
        return 'true'


s1=input()
s2=input()

print(checkPermutation(s1,s2))

