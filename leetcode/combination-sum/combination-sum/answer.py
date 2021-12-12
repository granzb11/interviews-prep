from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(comb, start):
            if len(comb) == k:
                combinations.append(list(comb))
                return
            elif len(comb) > k:
                return
            else:
                for i in range(start, n):
                    