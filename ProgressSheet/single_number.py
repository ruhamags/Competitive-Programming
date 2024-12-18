class Solution(object):
    def singleNumber(self, nums):
        unique = 0 
        for i in nums:
            unique ^= i
        return unique
       
            
            
        
        