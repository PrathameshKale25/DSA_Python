def Reverse(number):
    reversed=0
    while  number>0:
        reversed=reversed*10+number % 10
        number=number//10
    return reversed

number=100
print(Reverse(number))  
        
        
        
# def reverse_number(n):
#     reversed_num = 0
#     while n > 0:
#         reversed_num = reversed_num * 10 + n % 10
#         n = n // 10
#     return reversed_num

# # Example
# num = 12345
# print(reverse_number(num))  # Output: 54321
        