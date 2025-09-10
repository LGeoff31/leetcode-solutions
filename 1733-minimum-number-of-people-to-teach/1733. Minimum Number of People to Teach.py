from collections import defaultdict
from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Helper: do users a and b share any language?
        def has_common(a: List[int], b: List[int]) -> bool:
            sb = set(b)
            for x in a:
                if x in sb:
                    return True
            return False

        # 1) Find all users involved in friendships that cannot communicate
        bad_users = set()
        for u, v in friendships:
            if not has_common(languages[u - 1], languages[v - 1]):
                bad_users.add(u)
                bad_users.add(v)

        if not bad_users:
            return 0  # everyone already communicates

        # 2) Count, for each language, how many of these "bad" users already know it
        knows_count = defaultdict(int)
        for u in bad_users:
            for lang in languages[u - 1]:
                knows_count[lang] += 1

        # 3) Teach the language that the most "bad" users already know
        best_already_knows = max(knows_count.values(), default=0)
        need_to_teach = len(bad_users) - best_already_knows
        return need_to_teach
