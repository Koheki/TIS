A = [list(map(int,input().split())) for _ in range(3)]
N = int(input())
B = set([int(input()) for _ in range(N)])

for i in range(3):
    for j in range(3):
        if A[i][j] in B:

            if A[i][(j+1)%3] in B and A[i][(j+2)%3] in B:
                print("Yes")
                exit()
            if A[(i+1)%3][j] in B and A[(i+2)%3][j] in B:
                print("Yes")
                exit()

            if i == j:
                if A[(i+1)%3][(j+1)%3] in B and A[(i+2)%3][(j+2)%3] in B:
                    print("Yes")
                    exit()
                if i == 1:
                    if A[0][2] in B and A[2][0] in B:
                        print("Yes")
                        exit()

print("No")

