class Solution:
    # This has only one loop instead of two
    # While we step through the loop, we add earlier values to a dictionary: d[number] = index
    # This allows us to look up values more easily 
    # and prevents us from going through the loop more than once.  
    # Loop will end when we hit the second index of the pair
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create empty dictionary
        d = {}
        #start stepping through each value
        for i in range(len(nums)):
            #At index, find the complementary value needed
            val = target - nums[i]
            #see if that value is in the dictionary
            if val in d:
                #if so, return indices
                return d[val], i
            #otherwise add current list index to dict, then go back through loop
            else: d[nums[i]] = i
