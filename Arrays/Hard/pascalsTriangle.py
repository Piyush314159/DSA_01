class Solution:
	def nthRowOfPascalTriangle(self, n):
		row = [1]
		for i in range(1,n):
			if i==n:
				print(row)
			row = [1] + [row[j]+row[j+1] for j in range(len(row)-1)] +[1]
		return row
	
a = Solution()
print(a.nthRowOfPascalTriangle(5))