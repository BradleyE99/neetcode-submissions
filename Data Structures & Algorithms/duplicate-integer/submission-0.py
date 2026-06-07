class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result_set = set(nums)
        if len(result_set) < len(nums):
            return True
        else:
            return False