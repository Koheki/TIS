from collections import deque

N = int(input())
ST = [[n for n in input().split()] for _ in range(N)]

table = {t:s for s,t in ST}
setS = set([n[0] for n in ST])
start = []

for i in range(N):
    s,t = ST[i]
    if t not in setS:
        start.append(s)

que = deque(start)
changed = set()

while que:
    cur = que.popleft()
    changed.add(cur)

    while cur in table:
        changed.add(table[cur])
        cur = table[cur]

if len(changed) == N:
    print("Yes")
else:
    print("No")
