N,A,B = map(int,input().split())
S = input()

japanstudent = 0
overseastudent = 0

for s in S:
    if s == 'a':
        if japanstudent + overseastudent < A+B:
            print("Yes")
            japanstudent += 1

        else:
            print("No")
        
    elif s == 'b':
        if japanstudent + overseastudent < A+B and overseastudent < B:
            print("Yes")
            overseastudent += 1
        else:
            print("No")
    else:
        print("No")