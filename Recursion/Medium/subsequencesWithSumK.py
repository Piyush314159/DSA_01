class Solution:
    def perfectSum(self, arr, target):

        def sumSubsequence(i, s):

            if i >= len(arr) :
                return 1 if s == target else 0
            if s > target:
                return 0
            
            return sumSubsequence(i+1, s + arr[i]) + sumSubsequence(i+1, s)
        
        return sumSubsequence(0, 0)

sol = Solution()
print(sol.perfectSum([1, 3, 2, 4, 1], 4))

class Solution1:
    def perfectSum(self, arr, target):
        self.count = 0
        lst = []
        def subset(i, s, c):
            if i >= len(arr):
                if s == target:
                    lst.append(c[:])
                    self.count += 1
                return
            if s > target:
                return
            c.append(arr[i])
            subset(i+1, s + arr[i], c)
            c.pop()
            subset(i+1, s, c)
        subset(0, 0, [])
        return self.count, lst

sol1 = Solution1()
print(sol1.perfectSum([1, 3, 2, 4, 1], 4))