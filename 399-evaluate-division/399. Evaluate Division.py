class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        numerator: [(denominator, weight)]
        denominator: [(numerator, weight)]

        a: [(b, 2)]
        b: [(c, 3), (a, 1/2)]
        c: [(b, 1/3)]

        query: a/c
        goal: start from a, try to find c

        queue = [(c, 6)]

        WHEN IS IT NOT VALID?
        if a variable doesn't exist at all in numerator, 
        """
        number_equations = len(equations)
        conversions = defaultdict(list)

        for i in range(number_equations):
            n, d = equations[i]
            quotient = values[i]

            conversions[n].append((d, quotient))
            conversions[d].append((n, 1/quotient))
            conversions[n].append((n, 1))
            conversions[d].append((d, 1))

        res = []
        for n, d in queries:
            if n not in conversions:
                res.append(-1)
                continue
            
            queue = deque([den_weight for den_weight in conversions[n]])
            visited = set()

            while queue:
                den, weight = queue.popleft()
                if den in visited:
                    continue
                visited.add(den)
                
                if den == d:
                    res.append(weight)
                    break
                
                for new_den in conversions[den]:
                    den_2, weight_2 = new_den
                    queue.append((den_2, weight_2 * weight))
            else:
                res.append(-1)

        return res


