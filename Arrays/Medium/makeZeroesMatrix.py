class Solution:

    def makeZeros(self, mat):

        # 1. Find all original zeroes
        zeroes = []

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    zeroes.append([i, j])

        # 2. Calculate sums using original matrix
        sums = []

        for i, j in zeroes:
            total = 0

            if i > 0:
                total += mat[i-1][j]

            if i < len(mat)-1:
                total += mat[i+1][j]

            if j > 0:
                total += mat[i][j-1]

            if j < len(mat[i])-1:
                total += mat[i][j+1]

            sums.append(total)

        # 3. Make all neighbors of zeroes = 0
        for i, j in zeroes:

            if i > 0:
                mat[i-1][j] = 0

            if i < len(mat)-1:
                mat[i+1][j] = 0

            if j > 0:
                mat[i][j-1] = 0

            if j < len(mat[i])-1:
                mat[i][j+1] = 0

        # 4. Restore original zero positions with their sums
        for idx, (i, j) in enumerate(zeroes):
            mat[i][j] = sums[idx]

        return mat

a = Solution()
print(a.makeZeros([[1, 2, 3, 4],
                [5, 6, 0, 7], 
                [8, 9, 4, 6],
                [8, 4, 0, 2]]))