class Solution:
    def findPeakGrid(self, mat):
        lo, hi = 0, len(mat[0])-1

        while lo <= hi:
            mid = (lo + hi)//2

            # find the row with the maximum element in the mid column
            r = 0
            for i in range(len(mat)):
                if mat[i][mid] > mat[r][mid]:
                    r = i
            
            # check if the maximum element is a peak
            if mid > 0 and mat[r][mid-1] > mat[r][mid]:
                hi = mid-1
            elif mid < len(mat[0])-1 and mat[r][mid+1] > mat[r][mid]:
                lo = mid+1
            else:
                return f"{mat[r][mid]} is a peak element at index [{r}, {mid}]"
            
a = Solution()
print(a.findPeakGrid([[1,4],[3,2]]))
print(a.findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))
print(a.findPeakGrid([[14,15,16,17],[13,12,11,10],[9,8,7,6]]))