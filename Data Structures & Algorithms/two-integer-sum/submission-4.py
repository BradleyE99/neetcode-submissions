class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [] # Array
        
        for i in nums:
            j = nums.index(i) + 1
            number_needed = target - i
        
            while (j < len(nums)):
                if nums[j] == number_needed:
                    result.append(nums.index(i))
                    result.append(j)
                    return result
                else:
                    j += 1
                    continue
        return result
