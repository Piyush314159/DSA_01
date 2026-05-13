#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		for i in range(len(mat)):
			for j in range(len(mat[0])):
				if mat[i][j]==x:
					return [i,j]
			
a = Solution()
print(a.matSearch( [[3, 30, 38],[20, 52, 54],[35, 60, 69]], 35))
		