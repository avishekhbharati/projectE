def generateSumOfEvenFibonacciNumbers():
    firstNum = sumResult = 0
    secondNum = 1;
    
    while True:        
        result = firstNum + secondNum
        if result > 4000000:
            break
        elif result%2 == 0:
            sumResult += result
            
        firstNum = secondNum
        secondNum = result
    return sumResult
        
print(generateSumOfEvenFibonacciNumbers())
        
        
