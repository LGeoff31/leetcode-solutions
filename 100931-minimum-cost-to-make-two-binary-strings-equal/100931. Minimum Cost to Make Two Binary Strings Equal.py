class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        differences = 0
        n = len(s)
        a,b = sum(s[i] != t[i] for i in range(n) if (s[i] == '0' and t[i] == '1')), sum(s[i] != t[i] for i in range(n) if (s[i] == '1' and t[i] == '0'))
        # res = sum(s[i] != t[i] for i in range(n))
        option1 = min(swapCost, 2*flipCost)
        option2 = min(2*flipCost, crossCost + swapCost)
        return min(a,b) * option1 + (abs(a-b) // 2) * option2 + (abs(a-b)%2) * flipCost

        # figure which one is cheaper
        one_differences = abs(s.count("1") - t.count("1"))

        # We can either make that many toggles (one_differences * flipCost) OR we can make (crossCut * floor(one_differences / 2))
        option_1 = one_differences * flipCost
        option_2 = crossCost * floor(one_differences / 2)

        if option_1 < option_2:
            return one_differences * flipCost + (sum(s[i] != t[i]) - one_differences) // 2
        # Then we perform swapCost to make them identical
        else:
            lst_1 = list(s)
            lst_2 = list(t)
            cnt = 0
            one_differences //= 2
            for i in range(n):
                if lst_1[i] != lst_2[i] and cnt != one_differences:
                    lst_1[i], lst_2[i] = lst_2[i], lst_1[i]
                    cnt += 1
            print(lst_1, lst_2)
            
                    
            
            
            return crossCost * floor(one_differences / 2) + (sum(lst_1[i] != lst_2[i] for i in range(n)) // 2)

        # My concern is what if you would do a mixture of toggles 