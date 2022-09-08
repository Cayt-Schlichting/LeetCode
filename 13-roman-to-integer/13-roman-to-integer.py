class Solution:
    def romanToInt(self, s: str) -> int:
        #convert string to list
        l = list(s)
        #create translation dictionary
        conv = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        #convert romans to list of numbers
        l = [conv[i] for i in l]
        last = len(l)
        val = 0
        skip = False
        #loop over list
        for i, v in enumerate(l):
            #check if we need to skip this entry
            if skip: 
                #reset skip flag, then skip this loop
                skip = False
                continue
            #if last element of list, just add to total
            if i == last-1: 
                val += v
            elif v >= l[i+1]:
                #if this is >= next, add value to total
                val += v
            else:
                #add (next - this) to total
                val += l[i+1]-v
                #AND skip next value
                skip = True
        return val
        