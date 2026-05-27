'''
Max Product Subarray (Kadane's Variant):
    * Tracks both cur_max and cur_min at each step            → O(n)
    * Swaps max ↔ min when element is negative                → sign flip
    * Extends subarray or restarts from current element       → fresh start
    * Zero resets both products; answer preserved separately  → handles zeros
    * Space                                                    → O(1)

Args:
    * arr (list[int]) : non-empty list, may contain negatives/zeros

Returns:
    * int : largest product from any contiguous subarray

Example:
    * maxProduct([-2, 6, -3, -10, 0, 2])  →  180  ( 6 * -3 * -10 )
'''
class Solution:
	def maxProduct(self,arr):
		cur_max_prod = arr[0]
		curr_min_prod = arr[0]
		answer = arr[0]
		
		for i in range(1,len(arr)):
			
			if arr[i]<0:
				cur_max_prod, curr_min_prod = curr_min_prod, cur_max_prod
				
			cur_max_prod = max(cur_max_prod*arr[i], arr[i])
			curr_min_prod = min(curr_min_prod* arr[i], arr[i])
			
			answer = max(answer, cur_max_prod)
			print(cur_max_prod, curr_min_prod, answer)
		return answer
			
a = Solution()
print(a.maxProduct([8, -1, 0, 5, -4, 7, 5]))