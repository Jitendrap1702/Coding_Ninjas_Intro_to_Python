from itertools import groupby

def removeConsecutiveDuplicates(s):
    list=[]
    for char in s:
        list.append(char)

    print(''.join(k for k,g in groupby(list)))  #k=all unique caharcter in list
                                            #g=list of same character

s=input()

removeConsecutiveDuplicates(s)
