from sys import stdin

def bubbleSort(arr,n):
    for _ in range(n-1):
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
#Utility function for Fast I/O to take the input
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#Utility function to print the list
def printList(arr, n) : 
	for i in range(n) :
		print(arr[i], end = " ")
	print()


#main
arr, n = takeInput()
bubbleSort(arr, n)
printList(arr, n)
