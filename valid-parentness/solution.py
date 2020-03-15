class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if mapping[char] != top:
                    return False
        return not stack

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid(")"))