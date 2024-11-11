def Binary(arr,key):
    arr.sort()
    s=0
    e=len(arr)-1
   
    while s<=e:
        mid=s+(e-s)//2
        if key<arr[mid]:
            e=mid-1
          
        elif key>arr[mid]:
            s=mid+1
        else:
            return mid
            
    return -1

arr=[1,2,4,3,5,7,6]
key=6
print(Binary(arr,key))            