#takes a long time. Need to optimize
import datetime

def samallestMultiple():
    numTest = 11
    while True:
        for i in range(2, 21):
            if numTest%i != 0 :                
                break
            elif i == 20:
                return numTest
                
        numTest = numTest + 1
        
print(datetime.datetime.now())
print(samallestMultiple())
print(datetime.datetime.now())

