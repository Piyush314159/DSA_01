class Solution:
    def sortStack(self, st: list) -> list:
        # Base case: empty stack is already sorted
        if not st:
            return st
        
        # Step 1: Remove top element
        top = st.pop()
        
        # Step 2: Recursively sort the remaining stack
        self.sortStack(st)
        
        # Step 3: Insert top in its correct sorted position
        self.insertSorted(st, top)
        
        return st
    
    def insertSorted(self, st, element):
        # If stack is empty OR top is smaller than element, just push
        if not st or st[-1] >= element:
            st.append(element)
            return
        
        # Otherwise, pop top and recurse
        top = st.pop()
        self.insertSorted(st, element)
        
        # Put the popped element back
        st.append(top)

sol = Solution()
# Example usage:
print(sol.sortStack([34, 3, 31, 98, 92, 23]))  # Output: [3, 23, 31, 34, 92, 98]
print(sol.sortStack([3, 5, 1, 4, 2]))        # Output: [1, 2, 3, 4, 5]