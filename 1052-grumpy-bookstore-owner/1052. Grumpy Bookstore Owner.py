class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        lst = [0,0]
        global_loss = 0
        for i in range(len(customers) - minutes + 1): #[a,b,c,d,e] minutes = 2 -> [d,e]
            subarr = customers[i:i+minutes]
            loss = sum([customers[idx] for idx in range(i, i+minutes) if grumpy[idx] == 1])
            # print("subarr", subarr, loss)
            if loss > global_loss:
                lst[0], lst[1] = i, i+minutes-1
                global_loss = loss
        res = 0
        # print(lst)
        for i in range(len(customers)):
            if lst[0] <= i <= lst[1]:
                continue
            res += customers[i] if grumpy[i] == 0 else 0
        for i in range(lst[0], lst[1] + 1):
            res += customers[i]

        return res

        