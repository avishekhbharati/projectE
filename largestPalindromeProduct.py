def checkPalindrome(x):
    return str(x) == str(x)[::-1]

def compareResultWithListElement(y, myList):
    for elem in myList:
        if elem == y:
            return True                
    return False      

def largestPalindromeProduct():
    palindrome = 0
    duplication = False

    for i in range(100,1000):
        for j in range (100, 1000):
            res = i* j
            if checkPalindrome(res):                
                if res>palindrome:
                    palindrome = res
    return palindrome       

print(largestPalindromeProduct())


#print(largestPalindromeProduct())
'''
 num1 * all the 3 digits numbers
  if palindrome append to list 
 num2 * all the 3 digits numbers
  if palindrome
   if doesn't exist in list
    append to list
 get max from the list
  return value
'''  


 
 
