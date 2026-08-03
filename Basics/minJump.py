class Solution:
    def minJumps(self, list):
          if len(list) ==0:
                return -1
          if list[0]==0:
              return -1

          jump = 0
          max_reach = 0           # the right boundary of next layer
          curr_reach = 0          # the right boumdary of curr layer
          for i in range(len(list) - 1):
                max_reach = max(max_reach, i + list[i])
                
                if i == curr_reach:
                        jump += 1
                        curr_reach = max_reach

                if curr_reach <= i:
                    return -1
          return jump

s = Solution()
print(s.minJumps([1,3,5,8,9,2,6,7,6,8,9]))
print(s.minJumps([1,0,0,0]))