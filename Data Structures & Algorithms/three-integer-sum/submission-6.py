class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # Resulting Vector
        nums = sorted(nums) # Sort nums least to greatest


        for n in range(len(nums) - 2):
            if n > 0 and nums[n] == nums[n - 1]:
                continue # Don't include duplicates

            left, right = n + 1, len(nums) - 1
            target = -nums[n]


            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum == target: # if all three vals add to 0
                    res.append([nums[left], nums[right], nums[n]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return res

