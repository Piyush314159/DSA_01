class Solution:
    def find(self, nums, target):
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

        first = binarySearch(nums, target, findFirst=True)
        last = binarySearch(nums, target, findFirst=False)

        return [first, last]

a = Solution()
print(a.find([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))