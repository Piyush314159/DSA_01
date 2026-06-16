#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		r, c = 0, len(mat[0])-1

		while r < len(mat) and c >= 0:
			if mat[r][c] == x:
				return True

			elif mat[r][c] > x:				# decrease column
				c-=1
			else:							# increase row
				r+=1
		return False


a = Solution()
print(a.matSearch([[3, 30, 38],[20, 52, 54],[35, 60, 69]], 52))

'''
Input: mat[][] = [[3, 30, 38],[20, 52, 54],[35, 60, 69]], x = 62
Output: false
Explanation: 62 is not present in the matrix, so output is false.
'''