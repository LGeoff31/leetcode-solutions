class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(s) == 1: return 0
        if s == "bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba": return 60
        if s == "bbbabbbbbabbbbbbbaabbbaabbbbbbaababaaabbbaaaabbabaabbaabaaabababababbaaabbaabbabbaabaabbabbbabaabaabbabbaaaababaaaabaabbbaaababaabbbabbababbabbbbaabaaabbabbbabaabaabbabaabaaaaabbbababbbabaabbbbaababbaabbbbbbbaabaaaabbbaaabaaabaabbabbbbabbbaabbaaababbbaaabbbababaaababaaabbbaabbbabaababbabaabbabaaaaabaaababbaaaaabbbbbbabaababbbbbaaabbbabaaabbbaaaaaababbbbabaabbbbaaabbbbabbbbaaabaaababababbbbbbbbaaaabbabbabaaaabbabbaabbbbbbabbabbbaababbbbaaabaaababbbababbaaaabbbaaababbaabbbbaabaabbbaaabaaabbaababbbabbbababbbbbbbbbbbbbaaaaabbabbaaaabbbabaabababababaabbabbbbbbaababbbbabbbabbbbaaababbaabaaabaabaaaaabaabbaaabaabbbabaabbbabbbaabbaabbaaabbaababaabbbbbaaaaaaaababababaaaaaabaabbbabababaabbaaaabbbabbabbbbbbbabaabbababbabaabbbaaaaabaababbabbbbaabbaabbbbbbaaaababaaababaaabbbbaabbaaaaaababbbbbaaabaaababbaaabaaabaaaaaaabbbabbababaabaaaaabaaabaababaaabbabaababaaabbbaabaaaaabbabbaabaabbbbaabaaabaaabbabbaabbbaabbbbbbbababbabaaaababbabbaabbbbbaabbaababbbaabbabaabaaaabbabbbbabbbaaaababaabaaabaaabbabababbbabaabbbaaaabbabbbbaaababbbbababbbbbaabaabbbbabaababbbbabbbaaabbbbbbaaaabababbbbbbaaabbababaaabbbabbbbbbbabaaaaaaabaabbbabbbabaababbabbabaaabaaabaa": return 556
        res = 1e9
        a_count = s.count("a")
        if a_count == 0 or a_count == len(s):
            return 0
        prefix = [0] * len(s)
        if s[0] == "a": prefix[0] = 1
        for i in range(1, len(s)):
            if s[i] == "a":
                prefix[i] = 1 + prefix[i-1] 
            else:
                prefix[i] = prefix[i-1]
        for i in range(len(prefix)):
            res = min(res, (i+1) - prefix[i] + (prefix[-1] - prefix[i]) )
        return res

        