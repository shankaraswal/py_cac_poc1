def numFactorial(n):
    if n == 0:
        return 1
    else:
        return  n * numFactorial(n-1)
    
    
    
print (numFactorial(15))