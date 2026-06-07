class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # left pass: result[i] = product of everything left of i
        for n in range(len(nums) - 1):
            result[n + 1] = result[n] * nums[n]
        
        # Right pass: multiply in the product of everything right of i
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result