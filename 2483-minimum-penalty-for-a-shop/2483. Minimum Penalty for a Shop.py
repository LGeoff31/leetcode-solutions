class Solution:
    def bestClosingTime(self, customers: str) -> int:
        suffix_dic = Counter(customers)
        prefix_dic = defaultdict(int)
        res = float('inf')
        res = min(res, suffix_dic["Y"])
        closing_time = 0

        def penalty(suffix_dic, prefix_dic): 
            return suffix_dic["Y"] + prefix_dic["N"]

        for hour in range(len(customers)):
            suffix_dic[customers[hour]] -= 1
            prefix_dic[customers[hour]] += 1
            p = penalty(suffix_dic, prefix_dic)
            if p < res:
                closing_time = hour + 1
                res = p 
        
        return closing_time
