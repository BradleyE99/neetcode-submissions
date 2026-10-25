class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer 

        
        letters = s.replace(" ", "")
        l = "".join(filter(str.isalnum, letters)).lower()
        left, right = 0, len(l) - 1



        while left < right:
            
            if l[left] != l[right]:
                return False
            left += 1
            right -= 1
            
        return True
            