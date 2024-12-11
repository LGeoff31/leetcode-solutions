class Solution:
    def entityParser(self, text: str) -> str:
        res = ""
        idx = 0
        tags = {"&quot;":'"', "&apos;":"'", "&amp;":"&", "&gt;":">", "&lt;":"<", "&frasl;":"/"}
        while idx < len(text):
            print(text[idx])
            if idx+6 <= len(text) and text[idx:idx+6] == "&quot;":
                res += tags["&quot;"]
                idx += 6
            elif idx+6 <= len(text) and text[idx:idx+6] == "&apos;":
                res += tags["&apos;"]
                idx += 6
            elif idx+5 <= len(text) and text[idx:idx+5] == "&amp;":
                res += tags["&amp;"]
                idx += 5
            elif idx+4 <= len(text) and text[idx:idx+4] == "&gt;":
                res += tags["&gt;"]
                idx += 4
            elif idx+4 <= len(text) and text[idx:idx+4] == "&lt;":
                res += tags["&lt;"]
                idx += 4
            elif idx+7 <= len(text) and text[idx:idx+7] == "&frasl;":
                res += tags["&frasl;"]
                idx += 7
            else:
                res += text[idx]
                idx += 1
        return res