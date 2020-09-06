n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
def intersection(m,n,arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j]:
                print(arr1[i])
                arr2[j]=-10000
                break
            else:
                pass

intersection(m,n,arr1,arr2)
