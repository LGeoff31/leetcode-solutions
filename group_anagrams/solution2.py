class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idx = -1
        dic = {}

        def is_anagram(str1, str2):
            for char in str1:
                if str1.count(char) != str2.count(char):
                    return False
            return True

        for i in range(len(strs)):
            added = False
            curr_idx = 0
            while curr_idx < len(dic):
                if strs[curr_idx] == strs[i] and curr_idx != i:
                    dic[strs[i]] += "#"
                    added = True
                elif is_anagram(strs[i], strs[curr_idx]):
                    dic[strs[i]] = dic[strs[curr_idx]]
                    added = True
                curr_idx += 1

            if not added:
                idx += 1
                dic[strs[i]] = str(idx)
        length_2d_array = 0
        for key in dic:
            if "#" in dic[key]:
                length_2d_array = max(length_2d_array, int(
                    dic[key][:dic[key].index("#")]))
            else:
                length_2d_array = max(length_2d_array, int(dic[key]))
        print(dic)
        res = []
        for i in range(length_2d_array + 1):
            res.append([])

        for key in dic:
            number_hashtags = dic[key].count("#")
            for j in range(number_hashtags + 1):
                if "#" in dic[key]:
                    only_number = int(dic[key][:dic[key].index("#")])
                else:
                    only_number = int(dic[key])
                res[only_number].append(key)
        return res
