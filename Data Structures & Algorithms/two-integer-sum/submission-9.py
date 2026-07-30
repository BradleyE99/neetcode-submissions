class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [] # resulting indexes
        num_needed = 0 # current number needed 


        for i, n in enumerate(nums):
            num_needed = target - n

            if num_needed in nums[i+1:]:

                res.append(i)
                print(nums[i+1:])
                res.append(nums[i+1:].index(num_needed) + i + 1)
            else:
                continue
            return res


