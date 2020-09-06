# you can refer this image link for better understandings :-

https://files.codingninjas.in/0000000000004006.jpeg

def spiralPrint(arr):
    left=0
    top=0
    right=n-1
    bottom=m-1
    while True:
        #top_row
        if left>right:
            break
        for i in range(left,right+1):
            print(arr[top][i],end=' ')
        top=top+1
        
        #right_column
        if top>bottom:
            break
        for i in range(top,bottom+1):
            print(arr[i][right],end=' ')
        right=right-1

        #bottom_row
        if left>right:
            break
        for i in range(right,left-1,-1):
            print(arr[bottom][i],end=' ')
        bottom=bottom-1

        #left_column
        if top>bottom:
            break
        for i in range(bottom,top-1,-1):
            print(arr[i][left],end=' ')
        left=left+1

#Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
spiralPrint(arr)


