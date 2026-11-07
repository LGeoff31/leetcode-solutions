class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        """
        task assigned to server with smallest weight, tie broken by smallest index server
        
        what to do if available_servers is empty?? require waiting. inc current_time
        """

        tasks_association = [None] * len(tasks)
        available_servers = [(servers[i], i) for i in range(len(servers))] # minheap: (server_weight, server_idx)
        heapify(available_servers)
        current_time = 0 
        i = 0
        buffer = [] # minheap: (end_time, server_idx)

        while i < len(tasks):
            current_time = max(current_time, i)
            # compare buffer to current_time and restore all freely stored servers back into available_servers
            while buffer and buffer[0][0] <= current_time:
                end_time, server_idx = heappop(buffer)
                heappush(available_servers, (servers[server_idx], server_idx))
            
            # allocate tasks[i] to the top element in available_servers, if there's none, NO-OP and increment current)Time
            if not available_servers:
                current_time = buffer[0][0]
                continue
            
            server_weight, server_idx = heappop(available_servers)
            tasks_association[i] = server_idx
            heappush(buffer, (current_time + tasks[i], server_idx))
            i += 1
        
        return tasks_association
