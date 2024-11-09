def sort_0_1(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
       
        while left < right and arr[left] == 0:
            left += 1
       
        while left < right and arr[right] == 1:
            right -= 1
       
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    return arr

arr = [1, 0, 0, 0, 1, 1]
y = sort_0_1(arr)
print(y)
