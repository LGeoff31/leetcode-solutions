class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """ 
        AS YOU MOVE RIGHT
        1. You decrement the value at the left pointer (remove from sortedlist and decrement then add back)
        2. You increment the value at the right pointer (remove from sortedlist if exists, then increment, then add back)

        verify to see if the sum value changed, if not just add the new element, if yes the sum goes down by old * (old_amount - 1) and goes up by new * (new_amount + 1)

        """
        top = SortedList()
        rest = SortedList()
        freq = Counter()
        amount = 0

        def rebalance():
            nonlocal amount
            while rest and len(top) < x:
                f, v = rest.pop(0)
                top.add((f, v))
                amount += -f * -v
            
            while rest and top and rest[0] < top[-1]:
                f, v = rest.pop(0)
                f2, v2 = top.pop(-1)
                amount += f * v
                amount -= f2 * v2
                # swap
                top.add((f,v))
                rest.add((f2, v2))

        def update(n, d):
            nonlocal amount
            old_freq = freq[n]
            if old_freq:
                tup = (-old_freq, -n)
                if tup in top:
                    top.remove(tup)
                    amount -= old_freq * n
                else:
                    rest.remove(tup)

            freq[n] += d
            if freq[n]:
                rest.add((-freq[n], -n))

            rebalance()
        for i in range(k):
            update(nums[i], 1)
        res = [amount]
        for i in range(k, len(nums)): # O(n-k)
            update(nums[i-k], -1)
            update(nums[i], 1)
            res.append(amount)

        return res