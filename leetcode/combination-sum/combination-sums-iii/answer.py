from typing import List

class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        combinations = []
        def backtrack(remain, comb, start):
            # print("===============")
            # print(f"remain: {remain}")
            # print(f"comb: {comb}")
            # print(f"start: {start}")

            if remain == 0:
                combinations.append(list(comb))
                return
            #exceeds scope, stop exploring
            if remain < 0 or len(comb) == k:
                return

            for i in range(start, 10):

                # add candidate to combination
                comb.append(i)
                # give the current number another chance, rather than moving on
                backtrack(remain - i, comb, i+1)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 1)
        return combinations


combs = Solution().combinationSum3(3, 7)
print(combs)