class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_needed = 0

        for i, n in enumerate(nums):
            num_needed = target - n

            if num_needed in nums[i+1:]:
                return [i, nums[i+1:].index(num_needed) + i + 1]
            
        return []

