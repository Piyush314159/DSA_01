class Solution:
    
    def makeZeros(self, mat):
        zeroes = []
        
        for i in range(len(mat)): # store the coordinates of all zeroes in the matrix in a list called zeroes. 
            for j in range(len(mat[i])):
                if mat[i][j]==0:
                    zeroes.append([i,j])
        
        sums = [] #create an empty list called sums to store the sum of the adjacent elements for each zero in the zeroes list.
        for lst in zeroes:
            i, j = lst[0], lst[1]
            total = 0
            if i > 0: total += mat[i-1][j]
            if i < len(mat)-1: total += mat[i+1][j]
            if j > 0: total += mat[i][j-1]
            if j < len(mat[i])-1: total += mat[i][j+1]
            sums.append(total)
        
        for idx, lst in enumerate(zeroes): #iterate through the zeroes list and for each zero, set the adjacent elements.
            i, j = lst[0], lst[1]
            if i > 0: mat[i-1][j] = 0
            if i < len(mat)-1: mat[i+1][j] = 0
            if j > 0: mat[i][j-1] = 0
            if j < len(mat[i])-1: mat[i][j+1] = 0
            mat[i][j] = sums[idx] # set the values of zeroes to corespondind sum from sum list.
        
        return mat

a = Solution()
print(a.makeZeros([[1, 2, 3, 4],
                [5, 6, 0, 7], 
                [8, 9, 4, 6],
                [8, 4, 0, 2]]))