from sortedcontainers import SortedList
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capitals: List[int]) -> int:
        #your heap will have the elements you have enough capital to start, thus, you will remove the element with the highest profit using the heap

        #repeat this process k times
        #have a dictionary mapping capital to its avaialbe profits
        #lets say you currently have w, binary search for the largest capital you can afford with w
        #loop through the capitals up to that index and find the largest profit you can obtain, remove it from the map and update your w value

        #Overall time complexity: O(k * nlogn)

        #note that capital can become a set thats sorted after mapping
        dic = defaultdict(list)
        n = len(profits)
        for i in range(len(profits)):
            dic[capitals[i]].append(-profits[i])
        for key in dic:
            heapq.heapify(dic[key])
        capitals = list(set(capitals))
        capitals.sort()
        a = SortedList()
        # print(capitals)
        # print(dic)
        res = w
        prevIdx = 0
        for i in range(k):
            idx = bisect.bisect_right(capitals, res)
            print(idx)
            for c in capitals[prevIdx:idx]:
                for elem in dic[c]:
                    a.add(elem)

            if a: 
                res+=-a[0]
                a.discard(a[0])
            prevIdx = idx

        return res
        