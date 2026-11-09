import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # 1. Initialize all servers as idle and queue them before the first task.
        idle_before = list(range(k))
        idle_after = []
        busy_servs = []
        task_cnt = [0] * k
        
        # 2. Iterate through all tasks and sequentially update the server state variables.
        for task_idx, (start, duration) in enumerate(zip(arrival, load)):
            # 4. Calculate preferred server index for the current task using modulo logic.
            pref_id = task_idx % k
            
            # Reset the idle queues exactly when the preferred server wraps around to 0.
            if pref_id == 0:
                idle_after = idle_before
                idle_before = []
            
            # 5. Release all servers whose tasks are completed by the current start time.
            while busy_servs and busy_servs[0][0] <= start:
                free_time, serv_id = heapq.heappop(busy_servs)
                
                if serv_id < pref_id:
                    heapq.heappush(idle_before, serv_id)
                else:
                    heapq.heappush(idle_after, serv_id)
            
            # 6. Select the next available server from After queue, or Before queue.
            if idle_after:
                selected_id = heapq.heappop(idle_after)
            elif idle_before:
                selected_id = heapq.heappop(idle_before)
            else:
                continue # Drop the task entirely if no servers are currently idle.
                
            # 7. Assign task to server, update its processed count, and mark as busy.
            task_cnt[selected_id] += 1
            heapq.heappush(busy_servs, (start + duration, selected_id))
            
        # 3. Filter and collect all server ids matching the maximum processed task count.
        max_cnt = max(task_cnt)
        return [i for i, cnt in enumerate(task_cnt) if cnt == max_cnt]