from typing import Set


class Solution:
    def sort_num(self, num: int) -> int:
        return int("".join(sorted(str(num))))

    def countDigitOne(self, n: int) -> int:
        """
        count = 0
        for num in range(1, n + 1):
            count += str(num).count("1")
        return count
        """

        count = 0
        for num in range(1, n + 1):
            sorted_num = self.sort_num(num)
            if num % 10 == 0:
                count += str(num).count("1")
                continue

            if sorted_num < num:
                continue
            permutations = self.get_permutations(unprocessed=str(num))
            count_of_valid_permutations = len([i for i in permutations if i <= num])
            count += str(num).count("1") * count_of_valid_permutations
        return count

    def insert_at_idx(self, s: str, idx: int, val: str) -> str:
        return s[:idx] + val + s[idx:]

    def get_permutations(self, unprocessed: str, processed: str = "") -> Set[int]:
        if unprocessed == "":
            return {int(processed)}

        ans = set()
        for idx in range(len(processed) + 1):
            ans.update(
                self.get_permutations(
                    unprocessed=unprocessed[1:],
                    processed=self.insert_at_idx(processed, idx, unprocessed[0]),
                )
            )

        return ans


s = Solution()
assert s.countDigitOne(0) == 0
assert s.countDigitOne(1) == 1
assert s.countDigitOne(30) == 12
assert s.countDigitOne(21) == 13, s.countDigitOne(21)
