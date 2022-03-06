from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        1, 4, 7 => 1, 4, 8
        1, 4, 9 => 1, 5, 0
        3 => 4
        9 => 1, 0
        9, 9 => 1, 0, 0
        8, 9, 9 => 9, 0, 0
        """
        len_digits = len(digits)
        idx = -1

        while idx * -1 <= len_digits and digits[idx] == 9:
            digits[idx] = 0
            idx += -1

        if idx * -1 != len_digits + 1:
            digits[idx] += 1
            return digits

        ans = [1]
        ans.extend([0] * len_digits)
        return ans


s = Solution()
assert s.plusOne([1, 2, 3]) == [1, 2, 4]
assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
assert s.plusOne([3]) == [4]
assert s.plusOne([9]) == [1, 0]
assert s.plusOne([9, 9]) == [1, 0, 0]
assert s.plusOne([1, 4, 9]) == [1, 5, 0]
assert s.plusOne([8, 9, 9]) == [9, 0, 0]
