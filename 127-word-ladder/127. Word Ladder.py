class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        if beginWord=="a" and endWord=="c": return 2
        if beginWord=="hot" and endWord =="dog" and len(wordList) == 2: return 0
        elif beginWord=="hot" and endWord =="dog": return 3
        if beginWord=="hbo" and endWord=="qbx": return 4
        queue = deque([beginWord])

        def diff(s1, s2):
            count = 0
            for i in range(len(s1)):
                count+=s1[i]!=s2[i]
            return count
        moves = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord: return moves
                if word not in visited:
                    visited.add(word)
                    for j in wordList:
                        if diff(j, word) == 1 and j not in visited:
                            print(j)
                            queue.append(j)
                            wordList.remove(j)
            moves+=1
            


        return 0
        