class Solution:
    def isPalindrome(self, s: str) -> bool:
        
       
        norm_s = "".join(c.lower() for c in s if c.isalnum())
        p1 = 0
        p2 = len(norm_s) - 1
        while (p1 < p2):
            if (norm_s[p1] == norm_s[p2]):
                p1 += 1
                p2 -= 1
                continue
            else: 
                return False
        

        return True 