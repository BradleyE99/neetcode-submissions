class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        lo, hi = 0, (n * m) - 1

        while lo <= hi:
            mid = (hi + lo) // 2
            # Give middle of col (// n) and middle of row 
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False