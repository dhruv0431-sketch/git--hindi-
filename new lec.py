#function 
#write a program if the number is even count the factorial even and the no is odd count thr factorial odd 
# def  factorial (n): 
#     for i in range (1,n+1):
#         if n%i==0: 
#             print(i,end=" ")
#             return 10 
        
# x=factorial(12) 
# print(x)
# 
#  
# l 
# lst= eval(input("enter the list: "))
# print(type(lst)) 
# wap to take a list increase even no by 5 and decrease odd no by 5 

# Program to modify a number based on odd/even condition

# 
lst= eval(input("enter the list: "))
print(lst)
for i in range(len(lst)):
    if lst[i] % 2 == 0:  # Check if the number is even
        lst[i] += 5       # Increase even number by 5
    else:
        lst[i] -= 5       # Decrease odd number by 5
print(lst)