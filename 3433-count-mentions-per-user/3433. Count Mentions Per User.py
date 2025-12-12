class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        timestamps = {i : 0 for i in range(numberOfUsers)} # Tells what time it will be online
        res = [0] * numberOfUsers
        events.sort(key=lambda x: (int(x[1]), -ord(x[0][0])), reverse=False)

        print(events)
        for type, time, ppl in events:
            if type == "MESSAGE":
                if ppl == "ALL":
                    for i in range(numberOfUsers):
                        res[i] += 1
                elif ppl == "HERE":
                    for i in range(numberOfUsers):
                        res[i] += 1 if timestamps[i] <= int(time) else 0
                else:
                    id_lst = ppl.split()
                    for id in id_lst:
                        res[int(id[2:])] += 1
            else:
                timestamps[int(ppl)] = int(time) + 60
        return res
                     