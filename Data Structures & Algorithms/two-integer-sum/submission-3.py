class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        j = 0
        num_needed = 0
        for i in range(len(nums) - 1):
            num_needed = target - nums[i]
            j = i + 1
            while(j < len(nums)):
                if num_needed == nums[j]:
                    result.append(i)
                    result.append(j)
                    return result
                else:
                    j += 1
                    continue
        return result