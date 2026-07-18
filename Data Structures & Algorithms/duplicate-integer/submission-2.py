class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for n in nums:
            my_set.add(n)
        
        if len(my_set) < len(nums):
            return True
        else:
            return False