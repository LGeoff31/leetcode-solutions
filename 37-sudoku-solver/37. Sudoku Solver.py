from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        rows = defaultdict(set)      # was list -> set for O(1) membership
        cols = defaultdict(set)
        squares = defaultdict(set)
        currFilledIn = 0
        DIGITS = set("123456789")

        # init
        for r in range(n):
            for c in range(n):
                ch = board[r][c]
                if ch != ".":
                    currFilledIn += 1
                    rows[r].add(ch)
                    cols[c].add(ch)
                    squares[3 * (c // 3) + (r // 3)].add(ch)

        def dfs(currFilledIn: int) -> bool:
            if currFilledIn == 81:
                return True

            # MRV: pick the empty cell with the fewest candidates
            best = None
            best_cands = None

            for r in range(n):
                for c in range(n):
                    if board[r][c] == ".":
                        idx = 3 * (c // 3) + (r // 3)
                        used = rows[r] | cols[c] | squares[idx]
                        cands = DIGITS - used
                        if not cands:         # early prune
                            return False
                        if best is None or len(cands) < len(best_cands):
                            best = (r, c, idx)
                            best_cands = cands
                            if len(best_cands) == 1:
                                break
                if best is not None and len(best_cands) == 1:
                    break

            r, c, idx = best
            for ch in best_cands:
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                squares[idx].add(ch)

                if dfs(currFilledIn + 1):
                    return True

                # undo
                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                squares[idx].remove(ch)

            return False

        dfs(currFilledIn)
