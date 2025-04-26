class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        # m, n = len(grid), len(grid[0])
        # h_str = []
        # h_pos = []  
        # for i in range(m):
        #     for j in range(n):
        #         h_str.append(grid[i][j])
        #         h_pos.append((i, j))
        # # print(h_str)
        m, n = len(grid), len(grid[0])
        h_str = []
        h_pos = []  
        for i in range(m):
            for j in range(n):
                h_str.append(grid[i][j])
                h_pos.append((i, j))
        
        # get vertical string
        v_str = []
        v_pos = [] 
        for j in range(n):
            for i in range(m):
                v_str.append(grid[i][j])
                v_pos.append((i, j))

        def kmp_match_positions(s, pattern):
            n, m = len(s), len(pattern)
            res = [0] * (n + 1)  # using diff array idea
        
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length-1]
                    else:
                        lps[i] = 0
                        i += 1
        
            i = j = 0
            while i < n:
                if s[i] == pattern[j]:
                    i += 1
                    j += 1
                    if j == m:
                        res[i - m] += 1
                        res[i] -= 1
                        j = lps[j-1]
                else:
                    if j != 0:
                        j = lps[j-1]
                    else:
                        i += 1
        
            pre = 0
            mark = [False] * n
            for i in range(n):
                pre += res[i]
                if pre > 0:
                    mark[i] = True
            return mark
        h_mark = kmp_match_positions(h_str, pattern)
        v_mark = kmp_match_positions(v_str, pattern)

        ans = 0
        for idx in range(m * n):
            r, c = idx // n, idx % n
            i = c * m + r
            if h_mark[idx] and v_mark[i]:
                ans += 1
        
        return ans
        # # Given string s, find all the indexes that will generate pattern, classic kmp template
        # def kmp_match_positions(s, pattern, pos_map):
        #     n, m = len(s), len(pattern)
        #     res = set()
        
        #     lps = [0] * m
        #     length = 0
        #     i = 1
        #     while i < m:
        #         if pattern[i] == pattern[length]:
        #             length += 1
        #             lps[i] = length
        #             i += 1
        #         else:
        #             if length != 0:
        #                 length = lps[length-1]
        #             else:
        #                 lps[i] = 0
        #                 i += 1
        
        #     i = j = 0
        #     while i < n:
        #         if s[i] == pattern[j]:
        #             i += 1
        #             j += 1
        #             if j == m:
        #                 for k in range(m):
        #                     res.add(pos_map[i - m + k])
        #                 j = lps[j-1]
        #         else:
        #             if j != 0:
        #                 j = lps[j-1]
        #             else:
        #                 i += 1
        
        #     return res

        # # get horizontal string

        # # m, n = len(grid), len(grid[0])
        # # h_str = []
        # # h_pos = []  
        # # for i in range(m):
        # #     for j in range(n):
        # #         h_str.append(grid[i][j])
        # #         h_pos.append((i, j))
        # # print(h_str)

        # # get vertical string
        # v_str = []
        # v_pos = [] 
        # for j in range(n):
        #     for i in range(m):
        #         v_str.append(grid[i][j])
        #         v_pos.append((i, j))
    
        # m, n = len(grid), len(grid[0])
        # p_len = len(pattern)

        # horiz_cells = set() 
        # vert_cells = set()
        # # class kmp problem
        # # Horizontal pattern search with wrapping
        # for i in range(m):
        #     for j in range(n):
        #         x, y = i, j
        #         k = 0
        #         while k < p_len:
        #             if x >= m or grid[x][y] != pattern[k]:
        #                 break
        #             k += 1
        #             y += 1
        #             if y == n:
        #                 x += 1
        #                 y = 0
        #         if k == p_len:
        #             # match found
        #             x, y = i, j
        #             for kk in range(p_len):
        #                 horiz_cells.add((x, y))
        #                 y += 1
        #                 if y == n:
        #                     x += 1
        #                     y = 0

        # # Vertical pattern search with wrapping
        # for j in range(n):
        #     for i in range(m):
        #         x, y = i, j
        #         k = 0
        #         while k < p_len:
        #             if y >= n or grid[x][y] != pattern[k]:
        #                 break
        #             k += 1
        #             x += 1
        #             if x == m:
        #                 y += 1
        #                 x = 0
        #         if k == p_len:
        #             # match found
        #             x, y = i, j
        #             for kk in range(p_len):
        #                 vert_cells.add((x, y))
        #                 x += 1
        #                 if x == m:
        #                     y += 1
        #                     x = 0

        # return len(horiz_cells & vert_cells)
        # # print(v_str)
        # horz_matches = kmp_match_positions(h_str, pattern, h_pos)
        # vert_matches = kmp_match_positions(v_str, pattern, v_pos)
        # # print(horz_matches)
        # # print(vert_matches)
        # return len(horz_matches & vert_matches)
        # # horiz_cells = set()
        # # for idx in horiz_matches:
        # #     horiz_cells.add(h_pos[idx])
        # # vert_cells = set()
        # # for idx in vert_matches:
        # #     vert_cells.add(v_pos[idx])
        # # return len(horiz_cells & vert_cells)