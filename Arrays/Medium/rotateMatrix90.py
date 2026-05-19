'''
* Transpose the matrix
* Reverse each column(Anticlockwise) or reverse each row(Clockwise)
'''

class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if j>i:
                   mat[i][j], mat[j][i] = mat[j][i], mat[i][j]              #transpose the matrix by swapping the elements across the diagonal. We only need to swap elements where j>i to avoid swapping the same pair of elements twice.

        for j in range(n):
            top, bottom = 0, n-1                                            #reverse each column by swapping the elements from the top and bottom until they meet in the middle.
            while top<bottom:
                mat[top][j], mat[bottom][j] = mat[bottom][j], mat[top][j]   #swap the elements at the top and bottom of the column 
                top+=1
                bottom-=1
        
        return mat
    
a = Solution()
print(a.rotateMatrix([[0, 1, 2], 
                [3, 4, 5], 
                [6, 7, 8]]))