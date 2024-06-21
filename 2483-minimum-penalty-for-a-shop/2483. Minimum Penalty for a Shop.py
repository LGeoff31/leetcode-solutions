class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_count, n_count = customers.count("Y"), customers.count("N")
        curr_y = curr_n = 0
        res = 1e9
        dic = defaultdict(list)
        for hour in range(len(customers)):
            penalty = customers[hour] == "Y"
            penalty += curr_n + (y_count - curr_y - (customers[hour] == "Y"))
            if customers[hour] == "Y": curr_y += 1
            else: curr_n += 1
            dic[penalty].append(hour)
        dic[customers.count("N")].append(len(customers))
        print(dic)
        return dic[min(dic.keys())][0]
