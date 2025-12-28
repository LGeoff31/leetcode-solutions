class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        lst = []
        for f in favoriteCompanies:
            lst.append(set(f))
        bad_indicies = set()
        for i in range(len(lst)):
            for j in range(len(lst)):
                if i!=j and len(lst[i]) <= len(lst[j]) and len((lst[i] & lst[j])) == len(lst[i]):
                    bad_indicies.add(i)
                
        return list(i for i in range(len(favoriteCompanies)) if i not in bad_indicies)