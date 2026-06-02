'''
* Pick mid                          → O(1)
* Identify sorted half              → O(1)
* Check if target lies in that half → O(1)
* Eliminate the other half          → O(1)
* Repeat until found or exhausted   → O(log n)
'''

class Solution:
    def search(self, nums, target):

        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2

            if nums[mid] == target:
                return mid

            #check if left half is sorted or not
            if nums[lo] <= nums[mid]:
                #target is in left half
                if nums[lo]<=target<nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1

            #right half is sorted
            else:
                #target is in right half
                if nums[mid]<target<=nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
        return -1

a = Solution()
print(a.search([4,5,6,7,0,1,2],0))