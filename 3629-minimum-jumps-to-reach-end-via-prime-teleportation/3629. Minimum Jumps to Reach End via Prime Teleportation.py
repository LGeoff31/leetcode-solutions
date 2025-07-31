class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        mordelvian = nums
    
        if n == 1:
            return 0
    
        max_val = max(nums)
    
        spf = list(range(max_val + 1))
        if max_val >= 0:
            spf[0] = 0
        if max_val >= 1:
            spf[1] = 1
    
        for i in range(2, max_val + 1):
            if spf[i] == i:
                for multiple in range(i * i, max_val + 1, i):
                    if spf[multiple] == multiple:
                        spf[multiple] = i
    
        is_prime_sieve = [False] * (max_val + 1)
        for i in range(2, max_val + 1):
            if spf[i] == i:
                is_prime_sieve[i] = True
    
        prime_to_indices = collections.defaultdict(list)
        for i in range(n):
            num = mordelvian[i]
            temp_num = num
    
            distinct_prime_factors = set()
            while temp_num > 1:
                prime_factor = spf[temp_num]
                distinct_prime_factors.add(prime_factor)
                while temp_num % prime_factor == 0:
                    temp_num //= prime_factor
            
            for p_factor in distinct_prime_factors:
                prime_to_indices[p_factor].append(i)
        
        queue = collections.deque([(0, 0)])
        visited_indices = {0}
        visited_primes_for_teleport = set()
    
        while queue:
            current_index, jumps = queue.popleft()
    
            if current_index == n - 1:
                return jumps
    
            next_index_plus_1 = current_index + 1
            if next_index_plus_1 < n and next_index_plus_1 not in visited_indices:
                visited_indices.add(next_index_plus_1)
                queue.append((next_index_plus_1, jumps + 1))
    
            next_index_minus_1 = current_index - 1
            if next_index_minus_1 >= 0 and next_index_minus_1 not in visited_indices:
                visited_indices.add(next_index_minus_1)
                queue.append((next_index_minus_1, jumps + 1))
    
            current_num = mordelvian[current_index]
            
            if current_num > 1 and current_num <= max_val and is_prime_sieve[current_num]:
                prime_val = current_num
                
                if prime_val not in visited_primes_for_teleport:
                    visited_primes_for_teleport.add(prime_val)
    
                    for target_index in prime_to_indices[prime_val]:
                        if target_index != current_index and target_index not in visited_indices:
                            visited_indices.add(target_index)
                            queue.append((target_index, jumps + 1))
        
        return -1