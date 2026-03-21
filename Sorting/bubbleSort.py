class Solution:
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(0,n):
            swapped = False
            for j in range(0,n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    #
a = Solution()
print(a.bubbleSort([5, 3, 8, 1, 2]))

#   working of bubble sort is to repeatedly swap adjacent elements if they are in the wrong order.
#  The algorithm gets its name because smaller elements "bubble" to the top of the list (beginning) while larger elements sink to the bottom (end). 
# The process is repeated until the entire list is sorted.

# line by line explanation of the code:
# 1. We define a class named Solution.
# 2. We define a method named bubbleSort that takes an array (list) as input.
# 3. We calculate the length of the array and store it in variable n.
# 4. We start a loop that iterates from 0 to n-1 (inclusive) to control the number of passes through the array.
# 5. We initialize a boolean variable swapped to False at the beginning of each pass to track if any swaps were made.
# 6. We start another loop that iterates from 0 to n-1-i (inclusive) to compare adjacent elements. The -i is used to avoid comparing the last i elements, which are already sorted.
# 7. Inside the inner loop, we compare the current element (arr[j]) with the next element (arr[j+1]). If the current element is greater than the next element, we swap them and set swapped to True.
# 8. After the inner loop, we check if swapped is still False. If it is, it means no swaps were made, and the array is already sorted, so we break out of the loop.
# 9. Finally, we return the sorted array.