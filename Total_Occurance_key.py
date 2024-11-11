def Occurance(arr,key):
    s=0
    count=0
    arr.sort()
    e=len(arr)-1
    while s<=e:
        m=s+(e-s)//2
        if key<arr[m]:
            e=m-1
        elif key>arr[m]:
            s=m+1
        else:
            count+=1
            left=m-1
            right=m+1
            while left>=0 and arr[left]==key:
                count+=1
                left-=1 
        
            while right<len(arr) and arr[right]==key:
                count+=1
                right+=1
            break    
                    
    return count
arr=[1,2,3,3,3,3,4]
key=9
print(Occurance(arr,key))
            
    