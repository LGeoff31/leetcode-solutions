class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def is_almost_equal(x, y):
            s1 = str(x)
            s2 = str(y)
            
            max_len = max(len(s1), len(s2))
            s1 = s1.zfill(max_len)
            s2 = s2.zfill(max_len)

            diff_count = 0
            diff_index = []

            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff_count += 1
                    diff_index.append(i)
                    if diff_count > 2:
                        return False

            if diff_count == 0:
                return True
            if diff_count == 2:
                idx1, idx2 = diff_index

                # Swap characters
                s1_list = list(s1)
                s1_list[idx1], s1_list[idx2] = s1_list[idx2], s1_list[idx1]

                return ''.join(s1_list) == s2
            
            return False

        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if is_almost_equal(nums[i], nums[j]):
                    ans += 1

        return ans