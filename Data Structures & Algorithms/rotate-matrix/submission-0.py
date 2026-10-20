class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        l, r = 0, len(matrix) - 1

        while l < r:

            for i in range(r - l):
                top, bottom = l, r

                # Save top right in a variable
                topleft = matrix[top][l + i]

                # Move top left into bottom left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom left into bottom right
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move bottom right into top right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topleft
            l += 1
            r -= 1

        