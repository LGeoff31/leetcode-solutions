class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ 
        Idea: Create a graph where a node represents a word, and its edges are all the 
        other nodes which differ by a single letter

        1. brute force, wordList <= 10 but O(n^2)
        2. put all words in a freq hashmap, then look over each diff = 2
        """
        if endWord not in wordList:
            return 0
        word_list_set = set(wordList)
        
        queue = deque([beginWord])
        seen = {beginWord}
        cnt = 0
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return cnt + 1
                
                for i in range(len(word)):
                    for ch in range(26):
                        new_word = word[:i] + chr(ch + ord('a')) + word[i+1:]
                        if new_word in word_list_set and new_word not in seen:
                            seen.add(new_word)
                            queue.append(new_word)
            cnt += 1
        return 0

