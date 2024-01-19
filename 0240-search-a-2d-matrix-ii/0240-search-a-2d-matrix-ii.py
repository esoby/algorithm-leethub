class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            idx = bisect.bisect_left(row, target)

            if idx < len(row) and row[idx] == target:
                return True
        return False
