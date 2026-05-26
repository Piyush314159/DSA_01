class Solution:
	def mergeOverlap(self,arr):
		arr.sort()
		merged = []

		for lst in arr:
			start = lst[0]
			end = lst[1]
			if merged and start<=merged[-1][1]: 			#if the start of current interval in merged is less than the end of previous interval of merged
				merged[-1][1]=max(merged[-1][1], end)		#then update the end of the prvious interval
			else:
				merged.append([start,end])					#otherwise just append the new interval in the merged
		return merged
	
a = Solution()
print(a.mergeOverlap([[1, 3], [2, 6], [8, 9], [9, 11], [8, 10], [2, 4], [15, 18], [16, 17]]))