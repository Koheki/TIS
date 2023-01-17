import itertools

S,K = map(str,input().split())
K = int(K)-1

print(set(list(itertools.permutations(S))))
print("".join(set(list(itertools.permutations(S)))))