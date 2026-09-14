class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix) #rows
        n = len(matrix[0]) #cols

        l = 0
        r = m - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                break 
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        if l > r:
            return False

        row = mid

        l = 0
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False