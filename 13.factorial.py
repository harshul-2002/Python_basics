def calculate_factorial(n):
    if (n==1) or (n==0):
        return 1 
        
    else:
        return n * calculate_factorial(n - 1) 

print(calculate_factorial(5))   