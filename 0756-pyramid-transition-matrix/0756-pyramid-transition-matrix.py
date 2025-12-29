class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[a + b].append(c)

        @lru_cache(None)
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True

            def build(i, nxt):
                if i == len(row) - 1:
                    return dfs("".join(nxt))
                for c in mp.get(row[i:i+2], []):
                    nxt.append(c)
                    if build(i + 1, nxt):
                        return True
                    nxt.pop()
                return False

            return build(0, [])

        return dfs(bottom)

# class Solution:
#     def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
#         pair_to_top = defaultdict(list)
#         for pattern in allowed:
#             pair_to_top[(pattern[0], pattern[1])].append(pattern[2])

#         def can_build(row: str) -> bool:
#             if len(row) == 1:
#                 return True

#             def backtrack_next(i, next_row):
#                 if i == len(row) - 1:
#                     return can_build("".join(next_row))

#                 pair = (row[i], row[i + 1])
#                 if pair not in pair_to_top:
#                     return False

#                 for top in pair_to_top[pair]:
#                     next_row.append(top)
#                     if backtrack_next(i + 1, next_row):
#                         return True
#                     next_row.pop()

#                 return False

#             return backtrack_next(0, [])

#         return can_build(bottom)