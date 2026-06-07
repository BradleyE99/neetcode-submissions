class Solution:
    def isPalindrome(self, s: str) -> bool:
        use_s = "".join(i for i in s if i.isalpha() or i.isnumeric())
        
        p1 = 0
        p2 = len(use_s) - 1


        use_s = use_s.lower()
        print(use_s)
        while (p1 < p2):
            if (use_s[p1] == use_s[p2]):
                p1 += 1
                p2 -= 1
                continue
            else:
                return False

        return True        