class Solution:
    def kthElement(self, a, b, k):
        lo, hi = max(0, k-len(b)), min(k, len(a))

        while lo <= hi:
            i = (lo+hi)//2
            j = k-i

            a_left  = a[i-1] if i > 0 else float('-inf')
            a_right = a[i]   if i < len(a) else float('inf')
            b_left  = b[j-1] if j > 0 else float('-inf')
            b_right = b[j]   if j < len(b) else float('inf')

            if a_left > b_right:            # took too many from a
                hi = i-1
                '''
                The last element you picked from a is bigger than the first element you didn't pick from b.
                That means some element of b that should be in your left side isn't — you grabbed too much from a.
                '''
            
            elif b_left > a_right:          # took too many from b
                lo = i+1
                '''
                The last element you picked from b is greater than the first element you didn't pick from a.
                That means some element of a that should be in your left side isn't — you grabbed too much from b.
                '''
            else:                           # valid partition
                return(max(a_left, b_left))
    
a = Solution()
print(a.kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))