class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = 1e9
        dic = {}
        for i, word in enumerate(list2):
            if word not in dic:
                dic[word] = i
        
        for idx, word in enumerate(list1):
            if word in dic:
                if idx + dic[word] < res:
                    res = idx+dic[word]
                # res = min(res, idx + dic[word])
        ans = []
        for idx, word in enumerate(list1):
            if word in dic:
                if idx + dic[word] == res:
                    ans.append(word)
        return ans