class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(row, first, last):
            while first <= last:
                mid = (first + last) // 2

                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    first = mid + 1
                else:
                    last = mid - 1

            return False

        matrix_len = len(matrix)

        for index in range(matrix_len):

            # check whether target can exist in this row
            if matrix[index][0] <= target <= matrix[index][-1]:
                return binary_search(
                    matrix[index],
                    0,
                    len(matrix[index]) - 1
                )

        return False