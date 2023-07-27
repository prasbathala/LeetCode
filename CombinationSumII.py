from typing import List
def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
        res, n = [], len(candidates)
        candidates.sort()
        def dfs(i, target, path):
            if target == 0:
                res.append(path[:])
                return
            j = i
            while j < n:
                num = candidates[j]

                if target - num < 0:
                    j += 1
                    continue
                
                print(path)
                path.append(num)
                dfs(j + 1, target - num, path)
                path.pop()
                while j + 1 < n and candidates[j] == candidates[j + 1]:
                    j += 1
                j += 1
        dfs(0, target, [])
        return res
nums = [2, 5, 2, 1, 2]
target = 5
print(combinationSum2(nums, target))