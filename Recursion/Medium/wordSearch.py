class Solution:
    def exist(self, board, word):
        def backtrack(i, j, k):
            # 1. Base Case: Out of bounds
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):     
                return False

            # 2. Base Case: Character doesn't match
            if board[i][j] != word[k]:                                      
                return False
            
            # 3. Base Case: Found the whole word
            if k == len(word) - 1:                                          
                return True

            # 4. Mark as visited
            temp = board[i][j]
            board[i][j] = "#"

            # 5. Explore all 4 adjacent directions
            res = (backtrack(i+1, j, k+1) or 
                   backtrack(i, j+1, k+1) or 
                   backtrack(i-1, j, k+1) or 
                   backtrack(i, j-1, k+1))

            # 6. Backtrack (unmark)
            board[i][j] = temp
            
            return res

        # Start the DFS from every cell on the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False

s = Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))  # True
