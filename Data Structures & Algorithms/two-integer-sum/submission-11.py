class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        num_needed = 0

        for i, n in enumerate(nums):
            num_needed = target - n

            if num_needed in nums[i + 1:]:
                res.append(i)
                res.append(i + (nums[i + 1:]).index(num_needed) + 1)


        return res

