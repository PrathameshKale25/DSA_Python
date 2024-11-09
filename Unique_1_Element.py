def Unique(arr):
    a=len(arr)
    count=0
    arr.sort(reverse=True)
    print(arr)
    for i in range(0,a,1):
        if arr[i]!=arr[i+1]:
           return arr[i]
        else:
            return 0
arr=[1,1,2,3,2,1]  
k=Unique(arr)
print(k)      