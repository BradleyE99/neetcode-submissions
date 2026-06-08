class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}


        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 1
        for v in t:
            if v in t_map:
                t_map[v] += 1
            else:
                t_map[v] = 1

        return s_map == t_map       

            



       