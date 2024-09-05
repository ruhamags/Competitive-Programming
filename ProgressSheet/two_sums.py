class Solution(object):
    def twoSum(self, nums, target):
        final = {}
        for i, num in enumerate(nums):
            total = target - num
            if total in final:
                return[final[total], i]
            final[num] = i