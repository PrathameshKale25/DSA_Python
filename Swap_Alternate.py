def Swap_Array(arr):
    for i in range (0,len(arr),2):
        if i+1<len(arr):
            
            arr[i],arr[i+1]=arr[i+1],arr[i]
   
    return arr
arr=[1,2,3,4,5]
k=Swap_Array(arr)       
print(k)