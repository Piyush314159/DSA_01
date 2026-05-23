"""
* Sorting the array      → O(n log n)
* Fixing first element   → O(n)
* Fixing second element  → O(n)
* Two pointer search     → O(n)
* Overall                → O(n³)
* Space                  → O(1)
"""

class Solution:
    def fourSum(self, nums):
        nums.sort()                             # Sort the input array to facilitate the two-pointer technique and to easily skip duplicates
        res = []
        for i in range(len(nums)-3):            #fixing the first element and using two pointers to find pairs that sum up to the negative of the fixed element
            if i>0 and nums[i]==nums[i-1]:      
                continue
            for j in range(i+1,len(nums)-2):       #fixing the second element and checking the previous element to avoid duplicates
                if j>0 and nums[j]==nums[j-1]:
                    continue
                l, r = j+1, len(nums)-1             # Initialize two pointers, one starting just after the fixed element and the other at the end of the array
                while l<r:
                    s = nums[i]+nums[j]+nums[l]+nums[r]
                    if s>0:
                        r-=1
                    elif s<0:
                        l+=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:       # Skip duplicate elements for l to avoid duplicate triplets in the result
                            l+=1
                        while l<r and nums[r]==nums[r-1]:       # Skip duplicate elements for r to avoid duplicate triplets in the result
                            r-=1
                        l+=1
                        r-=1
        return res
    
a = Solution()
print(a.fourSum([1,0,-1,0,-2,2]))

# we are checking the previous elements for potential duplicates because we want catch the duplicates after their first occurance.
