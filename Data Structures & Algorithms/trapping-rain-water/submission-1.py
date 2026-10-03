class Solution:
    def trap(self, height: List[int]) -> int:
        # Dynamic Programming
        # Find max_left array
        # Find max_right array

        # Find max arrays first
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        i = 0
        j = len(height) - 1
        water_area = 0
        res = 0


        while i < len(height):
            if i == 0:
                left_max[i] = height[i]
            else:
                left_max[i] = max(height[i], left_max[i - 1])
            i += 1

        while j >= 0:
            if j == len(height) - 1:
                right_max[j] = height[j]
                
               
            else:
                right_max[j] = max(height[j], right_max[j + 1])
            j -= 1
      

        for k, n in enumerate(height):
            water_area = min(left_max[k], right_max[k]) - n
            if water_area > 0:
                res += water_area

        return res
        


        