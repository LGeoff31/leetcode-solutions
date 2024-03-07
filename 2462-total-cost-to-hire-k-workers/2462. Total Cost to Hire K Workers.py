import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n=len(costs)
        if 2*candidates>=n:
            costs.sort()
            return sum(costs[:k])
        df=n-(2*candidates)
        df2=df
        sm=0
        s1=costs[:candidates]
        s2=costs[n-candidates:]
        heapq.heapify(s1)
        heapq.heapify(s2)
        i=candidates
        j=n-candidates-1
        # print(costs[i],costs[j])
        ct=k
        while df>0 and k>0:
            x=heapq.heappop(s1)
            y=heapq.heappop(s2)
            if x<=y:
                sm+=x
                heapq.heappush(s1,costs[i])
                heapq.heappush(s2,y)
                i+=1
            else:
                sm+=y
                heapq.heappush(s1,x)
                heapq.heappush(s2,costs[j])
                j-=1
            df-=1
            k-=1
        lst1=heapq.nsmallest(min(k,len(s1)),s1)
        lst2=heapq.nsmallest(min(k,len(s2)),s2)
        lst=[]
        lst+=lst1[:]
        lst+=lst2[:]
        lst.sort()
        return sm+sum(lst[:k])

        