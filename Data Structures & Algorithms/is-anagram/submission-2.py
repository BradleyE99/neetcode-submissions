class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) # nlogn approach


        # if len(s) != len(t):
        #     return False

        # s_set = set(s)
        # t_set = set(t)

        # t_list = list(t_set)
        # s_list = list(s_set)

        # if len(t_list) != len(s_list):
        #     return False

        # for i in range(len(s_list) - 1):
        #     if t_list[i] != s_list[i]:
        #         return False
        #     else:
        #         continue
        # return True