#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		flat_arr = []
            
		for row in mat:
			for el in row:
				flat_arr.append(el)
		cols = len(mat[0])
				
		for i in range(len(flat_arr)):
			if flat_arr[i]==x:
				return[i//cols,i%cols]
			
a = Solution()
print(a.matSearch( [[3, 30, 38],[20, 52, 54],[35, 60, 69]], 35))
		