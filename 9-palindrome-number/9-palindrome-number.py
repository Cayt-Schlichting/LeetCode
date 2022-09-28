class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Go ahead and quit w/ False if x < 0
        if x<0: return False
        #vars to use
        i=0
        #convert number to list of digits
        l_x = list(str(x))
        while i < len(l_x) // 2:
            #Get second index spot
            i2 = -1 - i
            #Compare two index spots
            if l_x[i] == l_x[i2]: 
                # increment i and continue through loop
                i +=1
                continue
            else:
                return False
        #If we made it through the whole loop w/o exiting the function, it's a palindrome!
        return True
            
        