from itertools import groupby

def compressString(s):
    new=[list(g) for k,g in groupby(s)]
    for i in new:
        if len(i)==1:
            print(i[0],end='')
        else:
            print(i[0]+str(len(i)) ,end='')

    

s=input()
compressString(s)
