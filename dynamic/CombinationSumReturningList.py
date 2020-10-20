import math
import itertools as it
from collections import deque
from typing import List
from itertools import combinations

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    results = []
    def backtrack(num, target, path):
        if target == 0:
            results.append(path)
            return
        if num == len(candidates) or target < candidates[num]:
            return
        # then backtrack through candidates:
        backtrack(num, target - candidates[num], path + [candidates[num]])
        # then skip visited:
        backtrack(num + 1, target, path)
    backtrack(0, target, [])
    
    return results


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(combinationSum(0, candidates, target))
