def Duplicate(arr):
    arr.sort()
    unique=[]
    duplicate=[]
    for i in arr:
        if i in unique:
           if i not in duplicate:
            duplicate.append(i)
        else:
            unique.append(i)    
    return unique,duplicate
arr=[1,1,1,2,2,3,4,3,4,5,4,2,3,2,1,3,4,5,3,2,4,3,89,76,54,123,2123]
f= Duplicate(arr)
print(f)            