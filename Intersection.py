def Intersection(arr1,arr2):
    a=len(arr1)
    b=len(arr2)
    arr2.sort()
    arr1.sort()
    arr3=[]
    if b==0 or a==0 :
        return -1
    for i in range(0,a):
        for j in range(0,b):
            if arr2[j]==arr1[i]:
               arr3.append(arr1[i]) 
               break
    return arr3 if arr3 else -1
 
arr1=[1,6,5,4,3,2,8]
arr2=[1,2,3,4,9]           
g=Intersection(arr1,arr2)
print(g)           




# def Intersection(arr1, arr2):
#     # Find intersection using set and return result based on its existence
#     result = list(set(arr1) & set(arr2))
#     return result if result else -1

# # Test arrays
# arr1 = [1, 6, 5, 4, 3, 2, 8]
# arr2 = [1]
# g = Intersection(arr1, arr2)
# print(g)
