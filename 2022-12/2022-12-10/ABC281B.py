import string

U = string.ascii_uppercase

S = input()

if len(S) == 8:
    if S[0] in U and S[1:7].isdigit() and len(str(int(S[1:7]))) == 6 and S[7] in U:
        print("Yes")
        exit()
print("No")
