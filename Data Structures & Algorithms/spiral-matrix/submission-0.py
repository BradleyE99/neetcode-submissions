class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # need to rotate each element on outer edge until we reach the same element

        # if inner exists then move in and do same thing

        res = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom, = 0, len(matrix) - 1

        while left <= right and top <= bottom: 
            for i in range(left, right + 1):    # Left -> Right
                res.append(matrix[top][i])  
            top += 1
   
            # Count down
            for j in range(top, bottom + 1):    # Top right -> Bottom Right
                res.append(matrix[j][right])
            right -= 1

            # because top is changed we have to recheck
            if top <= bottom:
                # Count across bottom
                for k in range(right, left- 1, -1):
                    res.append(matrix[bottom][k])
                bottom -= 1


            # because right is changed, we have to recheck
            if left <= right:
                # count up until we reach len - 1
                for l in range(bottom, top - 1, -1):
                    res.append(matrix[l][left])
                left += 1
            
        return res
