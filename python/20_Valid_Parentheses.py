"""
Runtime : 0ms
Memory  : 16.72MB
"""


class Solution:
    def isValid(self, s: str) -> bool:
        next_close_list = []
        if len(s) == 1:
            return False
        for c in s:
            if c == "(":
                next_close_list.append(")")
            elif c == "[":
                next_close_list.append("]")
            elif c == "{":
                next_close_list.append("}")
            else:
                if next_close_list == []:
                    return False
                if c == next_close_list.pop():
                    continue
                else:
                    return False
        if next_close_list != []:
            return False
        return True


if __name__ == "__main__":
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("([])"))
