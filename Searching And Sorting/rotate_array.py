def rotate(arr, size, d):
    for i in range(size):
        if i<=d-1:
            for i in range(size-1):
                arr[i],arr[i+1]=arr[i+1],arr[i]
    
def takeInput() :
    n = int(input().strip())
    if n != 0:
        arr = [int(element) for element in list(input().strip().split())]
        return arr, n

    return list(), 0



def printList(arr, n) : 
	for element in arr :
		print(element, end = " ")
	print()


#main
arr, n = takeInput()
d = int(input().strip())

rotate(arr, n, d)
printList(arr, n)
