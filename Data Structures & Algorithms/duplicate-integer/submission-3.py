class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res_dict = dict()

        for n in nums:
            if n in res_dict:
                return True
            else:
                res_dict[n] = 0
        return False
        