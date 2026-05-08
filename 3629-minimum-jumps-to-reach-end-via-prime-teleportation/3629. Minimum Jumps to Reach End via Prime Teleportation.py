# Sieve of Eratosthenes to pre-calculate prime numbers up to MAX_RANGE
MAX_RANGE = (10**6) + 1
prime = [True] * MAX_RANGE
prime[0] = prime[1] = False

# The sieve algorithm to mark non-prime numbers
for i in range(2, int(sqrt(MAX_RANGE))):
    if prime[i] == True:
        for j in range(i*i, MAX_RANGE, i):
            prime[j] = False

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        maxi = 0
        val_to_index = defaultdict(list)
        # Pre-process to find the max value and map values to their indices
        for i in range(n):
            maxi = max(maxi, nums[i])
            val_to_index[nums[i]].append(i)

        visited = set() # To keep track of prime numbers for which teleportation is done
        dist = [float("inf")] * n # Distance array for BFS
        dist[0] = 0

        q = deque()
        q.append(0) # Start BFS from index 0

        while q:
            node = q.popleft() # Get the current index from the queue

            # Visit the left node, if it exists and hasn't been visited
            if node - 1 >= 0 and dist[node - 1] == float("inf"):
                q.append(node - 1)
                dist[node - 1] = 1 + dist[node]

            # Visit the right node, if it exists and hasn't been visited
            if node + 1 < n and dist[node + 1] == float("inf"):
                q.append(node + 1)
                dist[node + 1] = 1 + dist[node]

            # Teleport if the number at the current index is a prime and not yet used for teleportation
            if prime[nums[node]] == False or nums[node] in visited:
                continue

            i = 1
            # Iterate through multiples of the current prime number
            while True:
                new_node_val = nums[node] * i
                if new_node_val > maxi:
                    break

                # For each multiple, find all indices with that value and add them to the queue
                for new_node_index in val_to_index[new_node_val]:
                    if dist[new_node_index] == float("inf"):
                        q.append(new_node_index)
                        dist[new_node_index] = 1 + dist[node]

                i += 1

            # Mark this prime number as visited to avoid redundant teleports
            visited.add(nums[node])

            # Early exit if the last index is reached
            if dist[n - 1] != float("inf"):
                break
        
        # Return the minimum jumps to reach the end
        return dist[n - 1]