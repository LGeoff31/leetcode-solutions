class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l,r = 0, len(people) - 1
        res = 0
        people.sort()
        print(people)
        while l <= r:
            group = 1
            curr = people[r]
            while l < len(people) and curr + people[l] <= limit and group < 2:
                curr += people[l]
                group += 1
                l += 1
            r -= 1
            res += 1
            print(l, r)
        return res


