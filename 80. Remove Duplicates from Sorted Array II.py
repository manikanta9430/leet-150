from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
        

        k = 2

        for i in range(2, n):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k
        