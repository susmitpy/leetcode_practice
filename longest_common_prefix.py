from typing import List


class Solution:
    def get_common_prefix(self, str1: str, str2: str):
        common_prefix_last_index = -1
        for s1, s2 in zip(str1, str2):
            if s1 == s2:
                common_prefix_last_index += 1
            else:
                break

        if common_prefix_last_index == -1:
            return ""

        return str1[: common_prefix_last_index + 1]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Check if there is only one element in the input list
        try:
            second_elem = strs[1]
        except Exception:
            # There is only one element
            return strs[0]

        if strs[0] == "":
            return ""

        len_strs = len(strs)
        longest_common_prefix = strs[0]

        for i in range(1, len_strs):
            longest_common_prefix = self.get_common_prefix(
                longest_common_prefix, strs[i]
            )
            if longest_common_prefix == "":
                return ""

        return longest_common_prefix


s = Solution()

assert s.get_common_prefix("susmit", "susm") == "susm"
assert s.get_common_prefix("susmit", "susmits") == "susmit"
assert s.get_common_prefix("dog", "racecar") == ""

assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
