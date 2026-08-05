class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0
    

        for right, l in enumerate(s):
            

            while l in seen:
                seen.remove(s[left])
                left += 1
            seen.add(l)
            longest = max(longest, right - left + 1)
               
           
        return longest