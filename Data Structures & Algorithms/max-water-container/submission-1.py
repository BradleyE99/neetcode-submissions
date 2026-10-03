class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two pointers, start on each end
        
        p1, p2 = 0, len(heights) - 1
        curr_area = 0
        min_val = 0
        max_area = 0
        distance = 0

        while p1 < p2:

            distance = p2 - p1
      
            min_val = min(heights[p1], heights[p2])

            curr_area = min_val * distance
            max_area = max(max_area, curr_area)

            if heights[p1] > heights[p2]:
                p2 -= 1
            
            elif heights[p1] < heights[p2]:
                p1 += 1
            
            else:
                p2 -= 1

        return max_area