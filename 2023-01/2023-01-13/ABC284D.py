T = int(input())

for _ in range(T):
    N = int(input())
    p,q = 0,0
    for i in range(2,int((N)**(1/3))+1):
        if N%i != 0:
            continue
        if (N//i)%i == 0:
            p = i
            q = (N//i)//i
        else:
            p = int((N//i)**0.5)
            q = i
        break

    print(p,q)