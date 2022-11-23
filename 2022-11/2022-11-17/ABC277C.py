from collections import defaultdict

N = int(input())
ladder = defaultdict(list)

for _ in range(N):
    a,b = map(int,input().split())
    ladder[a].append(b)
    ladder[b].append(a)

visited = set()
visited.add(1)
stack = [1]

while stack:
    f = stack.pop()

    for g in ladder[f]:
        if g not in visited:
            visited.add(g)
            stack.append(g)

print(max(visited))