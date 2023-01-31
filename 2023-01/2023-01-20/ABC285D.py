from collections import deque

N = int(input())
ST = [[s for s in input().split()] for _ in range(N)]

table = {t:s for s,t in ST}
prev = set([s for s,_ in ST])

que = deque([])
for s,t in ST:
    if t not in prev:
        que.append(t)

changed = set()

while que:
    name = que.popleft()
    while name in table:
        changed.add(name)
        name = table[name]

if len(changed) == N:
    print("Yes")
else:
    print("No")