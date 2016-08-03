def samallestMultiple():
    numTest = 11
    while True:
        for i in range(2, 11):
            if numTest%i != 0:                
                break
            elif i == 10:
                print(numTest)       
                
        numTest = numTest + 1        

samallestMultiple()

'''
for each number starting from 2521
    check if number is divisible by all of the numbers from 1 to 20

def divisibleByAll(x):
    flag = False
    for i in range(1,20):
        if x%i != 0 :
            return False
        else :
            
        

def smallestMultiple():    
    numToTest = 2520
    while True:
        for i in range(1, 20):
            if numToTest % i != 0:
                 break;
            if i == 20 and numToTest % i == 0:
                return numToTest
                break
            
                
        numToTest += 2

print('smallest : '+ str(smallestMultiple()))
'''
