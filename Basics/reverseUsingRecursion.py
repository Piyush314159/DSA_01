class Solution:
    def reverseArray(self,arr,left,right):
        if left>=right:
            return
        arr[left],arr[right] = arr[right],arr[left]
        self.reverseArray(arr,left+1,right-1)
        return arr
    
a = Solution()
print(a.reverseArray([5,4,3,2,1],0,4))
