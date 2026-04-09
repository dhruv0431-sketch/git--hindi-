#function 
#write a program if the number is even count the factorial even and the no is odd count thr factorial odd 
def  factorial (n): 
    for i in range (1,n+1):
        if n%i==0: 
            print(i,end=" ")
            return 10 
        
x=factorial(12) 
print(x)
            