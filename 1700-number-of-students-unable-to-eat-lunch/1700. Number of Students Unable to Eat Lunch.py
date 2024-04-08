class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q1 = deque(students)
        q2 = deque(sandwiches)
        while True:
            if not q1: return 0
            if q2[0] not in q1: return len(q1)

            if q1[0] == q2[0]:
                q1.popleft()
                q2.popleft()
            else:
                q1.append(q1.popleft())
        

                

        