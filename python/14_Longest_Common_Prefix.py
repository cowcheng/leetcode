from typing import List

"""
Runtime : 3ms
Memory  : 16.54MB
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pat_str = strs[0]
        if len(strs) == 1:
            return strs[0]
        for i in range(1, len(strs[0]) + 1):
            for j in range(len(strs)):
                if strs[0][:i] != strs[j][:i]:
                    pat_str = strs[0][: i - 1]
                    return pat_str
        return pat_str


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
