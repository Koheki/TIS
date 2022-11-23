
que = deque([root])
res = 0

def perm(arr):
    pos = {m:j for j,m in enumerate(sorted(arr))}
    vis = [False]*len(arr)
    tot = 0
    for i in range(len(arr)):
        cnt = 0
        while not vis[i] and i != pos[arr[i]]:
            vis[i] = True
            i = pos[arr[i]]
            cnt += 1
        tot += max(0,cnt-1)
    return tot

while que:
    vals = []
    for _ in range(len(que)):
        n = que.popleft()
        vals.append(n.val)
        if n.left: que.append(n.left)
        if n.right: que.append(n.right)
    res += perm(vals)

return res