class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        l = len(beginWord)

        allwordList = collections.defaultdict(list)
        for word in wordList:
            for i in range(l):
                w = word[:i] +'*'+ word[i+1:]
                allwordList[w].append(word)

        que = collections.deque([[beginWord,1]])
        seen = set()
        seen.add(beginWord)

        while que:
            word,n = que.popleft()

            if word == endWord:
                return n

            for i in range(l):
                w = word[:i] +'*'+ word[i+1:]
                
                for g in allwordList[w]:
                    if g not in seen:
                        que.append([g,n+1])
                        seen.add(g)
        return 0

        