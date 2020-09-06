n=int(input())
arr=list(map(int,input().split()))
x=int(input())
def TripletSum(arr,n,x): 
  
    for i in range(0, n - 2):  
        for j in range(i + 1, n - 1):  
            for k in range(j + 1, n): 
                if (arr[i] + arr[j] + arr[k] == x):
                    a=max(arr[i],arr[j],arr[k])
                    b=min(arr[i],arr[j],arr[k])
                    print(b,' ',x-(a+b),' ',a)
                    

TripletSum(arr,n,x)
