class Solution:
    def rowWithMax1s(self, arr):
        max_count = 0
        max_row = -1
        for i in range(len(arr)):
            count = 0
            for j in range(len(arr[i])):
                if arr[i][j]==1:
                    count+=1
            if count> max_count:
                max_count = count
                max_row = i
        return max_row
    
a = Solution()
print(a.rowWithMax1s([[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]))