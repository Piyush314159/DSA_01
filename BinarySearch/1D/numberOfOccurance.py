class Solution:
    def countFreq(self, arr, target):
        def binarySearch(nums, target, findFirst):
            lo, hi = 0, len(nums)-1
            idx = -1

            while lo<=hi:
                mid = (lo+hi)//2

                if nums[mid]==target:
                    idx = mid

                    if findFirst:
                        hi = mid-1
                    else:
                        lo = mid+1

                elif nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid-1
            return idx

        first = binarySearch(arr, target, findFirst=True)
        if first==-1:
            return 0
        last = binarySearch(arr, target, findFirst=False)

        return (last-first)+1

a = Solution()
print(a.countFreq([8, 9, 10, 12, 12, 12], 12))
