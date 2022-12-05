class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                p = []
                while stack[-1] != '[':
                    p.append(stack.pop())
                stack.pop()
                l,b = 0,0
                while stack and stack[-1].isdigit():
                    l += int(stack.pop())*10**b
                    b +=1
                for _ in range(l):
                    stack.extend(p[::-1])

            else:
                stack.append(c)

        return "".join(stack)