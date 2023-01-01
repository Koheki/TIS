S = input()

res = True
chars = set()
stack = []

for i in range(len(S)):
    if 97 <= ord(S[i]) <= 122:
        if S[i] in chars:
            res = False
            break
        else:
            chars.add(S[i])
            stack.append(S[i])
    elif S[i] == '(':
        stack.append('(')
    else:
        j = len(stack)-1
        while j > 0 and stack[j] != '(':
            p = stack.pop()
            chars.discard(p)
            j-=1
        stack.pop()

if res:
    print("Yes")
else:
    print("No")