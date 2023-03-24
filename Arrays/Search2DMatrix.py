#LC-74
#Search element in sorted 2d array, log(mn)

class Solution(object):

    def searchMatrix(self, matrix, target):
        first_col_arr = [row[0] for row in matrix]
        row = self.binarySearch(first_col_arr, target)
        col = self.binarySearch(matrix[row], target)
        return matrix[row][col] == target
    
    def binarySearch(self, arr, target):
        l = 0
        r = len(arr)-1
        while(l<=r):
            m = (l+r)//2
            if target < arr[m]:
                r=m-1
            elif target > arr[m]:
                l=m+1
            else:
                return m
        return l-1

    