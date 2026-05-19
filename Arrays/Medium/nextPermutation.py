'''
* Finding pivot → O(n)
* Finding swap element → O(n)
* Reversing suffix → O(n)
'''
class Solution:  
    def nextPermutation(self, arr):
        n = len(arr)
        i=n-2
        j=n-1
        pivot = -1

        #finding the pivot
        while i>=0:
            if arr[i]<arr[i+1]:
                pivot = i
                break
            i-=1

        #edge case
        if pivot==-1:
            l = 0
            r = n-1
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1

        else:
            #finding the swaping element
            while j>pivot:
                if arr[j]>arr[i]:
                    swap = j
                    break
                j-=1
            arr[pivot], arr[swap] = arr[swap], arr[pivot]

            #now reversing suffix elements
            l = i+1
            r = n-1
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1

        return arr
    
a = Solution()
print(a.nextPermutation([2, 4, 1, 7, 8, 6, 3])) 