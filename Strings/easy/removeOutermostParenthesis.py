class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0
        for ch in s:
            if ch == "(":
                if depth > 0:           #before adding the opening parenthesis, check if depth is greater than 0
                    result.append(ch)   #if depth is greater than 0, add the opening parenthesis to the result
                depth += 1              #increment depth for every opening parenthesis
            else:   # ch == ")"
                depth -= 1              #decrement depth for every closing parenthesis
                if depth > 0:           #before adding the closing parenthesis, check if depth is greater than 0
                    result.append(ch)
        return "".join(result)
    
a = Solution()
print(a.removeOuterParentheses("(()())(())"))  # Output: "()()()"
print(a.removeOuterParentheses("(()())(())(()(()))"))  # Output: "()()()()(())"
print(a.removeOuterParentheses("()()"))  # Output:""
print(a.removeOuterParentheses("((()))"))  # Output: "(())"