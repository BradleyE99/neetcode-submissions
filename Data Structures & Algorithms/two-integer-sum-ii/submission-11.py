class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # increasing order (1-indexed)

        # ex: [1, 2, 3, 4]  
        num_needed = 0
        
        
        for n in range(len(numbers) - 1):
            left, right = n + 1, len(numbers) - 1
            
            num_needed = target - numbers[n]

            while left <= right:
                mid = (left + right) // 2
                # binary search approach
                if num_needed > numbers[mid]:
                    left = mid + 1
                elif num_needed < numbers[mid]:
                    right = mid - 1
                else:
                    return [n + 1, mid + 1]


        return []
# [1, 2, 3, 4], t = 3
# mid = 2, num_needed = 2
# 2 == 2 , return [1, 3]
        


