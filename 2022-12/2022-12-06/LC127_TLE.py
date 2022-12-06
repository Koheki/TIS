class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        que = collections.deque([[beginWord,1]])
        seen = set()
        seen.add(beginWord)

        while que:
            word,n = que.popleft()

            if word == endWord:
                return n

            for w in wordList:
                if w not in seen:
                    c = 0
                    for i,j in zip(word,w):
                        if i != j:
                            c += 1
                        if c > 1:
                            break
                    if c == 1:
                        que.append([w,n+1])
                        seen.add(w)

        return 0
