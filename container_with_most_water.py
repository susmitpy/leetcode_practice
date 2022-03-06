# https://leetcode.com/problems/container-with-most-water/
from typing import List
from json import load


class Solution:
    def maxArea(self, height: List[int]) -> int:
        areas = []
        len_height = len(height)

        for left_idx, left_height in enumerate(height[:-1]):
            for right_idx in range(left_idx + 1, len_height):
                area = min(left_height, height[right_idx]) * (right_idx - left_idx)
                areas.append(area)

        return max(areas)


s = Solution()
assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert s.maxArea([1, 1]) == 1

inputs = load(open("./inputs/container_with_most_water.json"))
assert s.maxArea(inputs["0"]) == 48431514
