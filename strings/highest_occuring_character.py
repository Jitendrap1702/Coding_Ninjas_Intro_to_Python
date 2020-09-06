def HighestOccurrCharacter(s):
    total_char=256
    count=[0]*total_char
    for char in s:
        count[ord(char)]+=1
    
    greatest=count[ord(s[0])]
    ans=s[0]
    for char in s:
        if count[ord(char)]>greatest:
            ans=char
            greatest=count[ord(char)]

    return ans

s=input()

result=HighestOccurrCharacter(s)
print(result)
