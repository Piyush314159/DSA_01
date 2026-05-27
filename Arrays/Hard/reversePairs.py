class Solution:
    def reversePairs(self, nums):
        self.count = 0
        temp = [0] * len(nums)   # ← allocated ONCE

        def mergeSort(arr, l, r):
            if l >= r:
                return

            mid = (l + r) // 2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, r)

            # PASS 1 — count
            i = l
            j = mid + 1
            while i <= mid and j <= r:
                if arr[i] > 2 * arr[j]:
                    self.count += (mid - i + 1)
                    j += 1
                else:
                    i += 1

            # PASS 2 — merge into temp
            i = l
            j = mid + 1
            k = l
            while i <= mid and j <= r:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            while j <= r:
                temp[k] = arr[j]
                j += 1
                k += 1

            # copy back from temp to arr
            for k in range(l, r + 1):
                arr[k] = temp[k]

        mergeSort(nums, 0, len(nums) - 1)
        return self.count

a = Solution()
print(a.reversePairs([1, 3, 2, 3, 1]))  # Output: 2
