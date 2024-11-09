def Triplet(target,arr):
    a=len(arr)
    arr1=[]
    for i in range(0,a):
        for j in range(i+1,a):
            for k in range(j+1,a):
                if arr[i]+arr[j]+arr[k]==target:
                    arr1.append((arr[i],arr[j],arr[k]))
                    
    return arr1
arr=[1,2,3,4,5,6,7,8,9,10]
target=10
print(Triplet(target,arr))                