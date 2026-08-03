class Solution:
    def reverseStack(self, st):
        def reverse(l, r):

            if l >= r:
                return

            st[l], st[r] = st[r], st[l]
            reverse(l+1, r-1)

        reverse(0, len(st)-1)
        return st
            
sol = Solution()
# Example usage:
print(sol.reverseStack([1, 2, 3, 4, 5]))