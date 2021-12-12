from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        candidates.sort()
        def backtrack(remain, comb, start):
            # got a combination, add to list and return
            if remain == 0 and list(comb) not in combinations:
                combinations.append(list(comb))
                return
            # exceeded, no need to explore
            elif remain < 0:
                return
            else:
                for i in range(start, len(candidates)):
                    # add candidate to combination
                    comb.append(candidates[i])
                    # give the current number another chance, rather than moving on
                    backtrack(remain - candidates[i], comb, i+1)
                    # backtrack, remove the number from the combination
                    comb.pop()

        backtrack(target, [], 0)
        return combinations

candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates, target))


