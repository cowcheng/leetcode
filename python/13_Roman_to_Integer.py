"""
Runtime : 5ms
Memory  : 16.60MB
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_list = ["I", "V", "X", "L", "C", "D", "M"]
        value_list = [1, 5, 10, 50, 100, 500, 1000]

        s_len = len(s)
        if s_len == 1:
            return value_list[roman_list.index(s)]

        cur_index = roman_list.index(s[0])
        tmp_num = value_list[cur_index]

        for i in range(1, s_len):
            tmp_index = roman_list.index(s[i])
            if value_list[tmp_index] > value_list[cur_index]:
                tmp_num += value_list[tmp_index] - 2 * value_list[cur_index]
            else:
                tmp_num += value_list[tmp_index]
            cur_index = tmp_index

        return tmp_num


if __name__ == "__main__":
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))
