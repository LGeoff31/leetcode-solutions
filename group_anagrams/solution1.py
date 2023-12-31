class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_lst = []
        for i in range(len(strs)):
            sorted_lst.append(''.join(sorted(strs[i])))

        visited = set()
        unique_elements = 0

        for i in range(len(sorted_lst)):
            if sorted_lst[i] not in visited:
                visited.add(sorted_lst[i])
                unique_elements += 1
        res = []
        for i in range(unique_elements):
            res.append([])

        curr_idx = 0
        a = set()
        for i in range(len(sorted_lst)):  # O(n)
            curr_string = sorted_lst[i]
            if curr_string not in a:
                a.add(curr_string)
                res[curr_idx].append(strs[i])
                for j in range(i+1, len(sorted_lst)):  # O(n)
                    if sorted_lst[j] == curr_string:
                        res[curr_idx].append(strs[j])
                curr_idx += 1

        return res
