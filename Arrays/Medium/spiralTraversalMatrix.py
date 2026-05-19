'''
* Spiral traversal with 4 boundaries (top, bottom, left, right) → O(1) space
* Traverse top row left→right, right col top→bottom, bottom row right→left, left col bottom→top
* Shrink boundaries after each traversal → ensures no element visited twice
* Count elements as traversed, return when count == k → O(n×m) time
'''

class Solution:
    def findK(self, mat, k):
        top, bottom, left, right = 0, len(mat)-1, 0, len(mat[0])-1
        count = 0
        while top<=bottom and left<=right:
            for i in range(left, right+1): # traverse top row from left to right
                count+=1
                if count==k:
                    return mat[top][i]
            top+=1

            for i in range(top, bottom+1): # traverse right column from top to bottom
                count+=1
                if count==k:
                    return mat[i][right]
            right-=1

            if top<=bottom:
                for i in range(right, left-1, -1):# traverse bottom row from right to left
                    count+=1
                    if count==k:
                        return mat[bottom][i]
                bottom-=1

            if left<=right:
                for i in range(bottom, top-1, -1): # traverse left column from bottom to top
                    count+=1
                    if count==k:
                        return mat[i][left]
                left+=1
        return -1

a = Solution()
print(a.findK([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]], 4))