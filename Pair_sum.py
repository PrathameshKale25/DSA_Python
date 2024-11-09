def pair_sum(arr,target):
    s=[]
    
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            
            if arr[i]+arr[j]==target:   
               s.append((arr[i],arr[j]))
    return s
arr=[1,2,3,4,5,6,7,8,9]
target=5
g=pair_sum(arr,target)
print(g)   