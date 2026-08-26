class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row = 0
        right_row = len(matrix)-1
        while (left_row<=right_row):
            middle_row = int((left_row + right_row)/2)
            if target>matrix[middle_row][len(matrix[middle_row])-1]:
                left_row = middle_row + 1
            elif target<matrix[middle_row][0]:
                right_row = middle_row -1
            else:
                left = 0
                right = len(matrix[middle_row])-1
                while(left<=right):
                    middle = int((left+right)/2)
                    if target>matrix[middle_row][middle]:
                        left = middle+1
                    elif target<matrix[middle_row][middle]:
                        right = middle-1
                    elif target==matrix[middle_row][middle]:
                        return True
                return False
        return False        