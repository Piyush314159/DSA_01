class Solution:
	def minJumps(self, arr):
		
		if len(arr) ==0:
			return -1
		
		if arr[0]==0:
			return -1
		
		jumps=0
		max_reach=0
		current_end = 0

		for i in range(len(arr)-1):
			max_reach = max(max_reach, i+arr[i])
			
			if i==current_end:
				jumps+=1
				current_end=max_reach

				if current_end<=i:
					return -1
				
		return jumps