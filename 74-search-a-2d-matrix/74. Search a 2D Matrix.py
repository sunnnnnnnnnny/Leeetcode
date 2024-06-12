class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first need to determine which row it might be located
        # thus the search would be O(logN)
        # Second search within the row =>time O(logM)
        # Overall using 2 binary search => time O(logMN)
        # space: O(1) as constants only
        rows = [x[0] for x in matrix ]
        # print(rows)
        # def leftBinary(nums):
        #     left = 0
        #     right = len(nums)-1
        #     while left<=right:
        #         mid = left+(right-left)//2
        #         print(left, right, mid)
        #         print(nums[mid])
        #         if nums[mid]>=target:
        #             if nums[mid]==target:
        #                 return mid
        #             right = mid-1
        #         else:
        #             left = mid+1
        #     return left
        
        def rightBinary(nums):
            left = 0
            right = len(nums)-1
            while left<=right:
                mid = left+(right-left)//2
                # print(left, right, mid)
                # print(nums[mid])
                if nums[mid]<=target:
                    if nums[mid]==target:
                        return mid
                    left = mid+1
                else:
                    right = mid-1
            return right
        rowLoc = rightBinary(rows)
        # print(rowLoc)
        if rows[rowLoc] == target:
            return True
        colLoc = rightBinary(matrix[rowLoc])
        if matrix[rowLoc][colLoc] == target:
            return True
        return False
        