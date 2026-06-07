class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        nums_list = list(nums_set)
        if len(nums_list) != len(nums):
            return True
        else:
            return False
