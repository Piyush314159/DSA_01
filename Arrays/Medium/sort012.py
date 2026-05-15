'''
Dutch National Flag Algorithem
'''

class Solution:
    def sort012(self, arr):
        low = mid = 0
        high = len(arr)-1

        while mid<=high:
            if arr[mid]==0:  # both low and mid are 0, we can just move both forward
                arr[mid], arr[low] = arr[low], arr[mid]
                mid+=1
                low+=1
            elif arr[mid]==1: # mid is 1, we can just move mid forward
                mid+=1
            else: #
                arr[mid], arr[high] = arr[high], arr[mid]
                high-=1
        return arr

a = Solution()
print(a.sort012([0,1,2,0,1,2]))