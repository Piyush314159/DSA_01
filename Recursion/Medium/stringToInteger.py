class Solution:
    def atoi(self, s):
        def helper(s, index, result, sign, started):        # sign -> int {+1, -1}
            if index == len(s):
                return sign * result

            ch = s[index]

            if ch == " " and not started:
                return helper(s, index + 1, result, sign, started)

            if ch in("+", "-") and not started:
                if ch == '+' :
                    return helper(s, index + 1, result, 1, True)

                if ch == '-' :
                    return helper(s, index + 1, result, -1, True)

            if ch.isdigit():
                new_res = result * 10 + int(ch)
                return helper(s, index + 1, new_res, sign , True)

            return sign * result
        
        result = helper(s, 0, 0, 1, False)

        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        
        return result

sol = Solution()
# Test cases
print(sol.atoi("42"))  # Output: 42
print(sol.atoi("   -42"))  # Output: -42
print(sol.atoi("4193 with words"))  # Output: 4193
print(sol.atoi("words and 987"))  # Output: 0