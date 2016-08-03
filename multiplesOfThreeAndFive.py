def getMultiples(num1, num2, belowNum):
    sum = 0
    for i in range(1, belowNum):
        if i%num1 == 0 or i%num2 == 0:
            sum += i
    return sum

print(getMultiples(3, 5, 1000))
        
        
        
    
    
