class Solution:
	def nthRowOfPascalTriangle(self, n):
		row = [1] 									# First row of Pascal's triangle
		for i in range(1,n):
			new_row = [1] 							# First element of each row is always 1
			for j in range(len(row)-1):
				new_row.append(row[j]+row[j+1])		# Each element (except the first and last) is the sum of the two elements directly above it in the previous row
			new_row.append(1) 						# Last element of each row is always 1
			row = new_row							# Update row to the new row for the next iteration
			if i==n-1:
				print(row)							# Print the nth row of Pascal's triangle
	
a = Solution()
a.nthRowOfPascalTriangle(5)