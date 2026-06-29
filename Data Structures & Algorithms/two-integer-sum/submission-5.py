class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        for i, n in enumerate(nums):
            num_needed = target - n

            if num_needed in nums[i + 1:]: # O(n) search
                
                res.append(i)
                res.append(nums[i + 1:].index(num_needed) + (i + 1))
                return res
            else:
                continue
        return res