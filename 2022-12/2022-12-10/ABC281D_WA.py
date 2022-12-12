N,K,D = map(int,input().split())
A = sorted([int(n) for n in input().split()],reverse=True)

odd = [a for a in A if a % 2 == 1]
even = [a for a in A if a%2 == 0]

if D % 2 == 0:
    if K%2 == 1 and len(even) == 0:
        print(-1)
    else:
        oi,ei = K//2,K%2
        if K %2 == 0:
            sumodd = sum(odd[:oi+1])
            sumeven = 0
            ei = -1
        else:
            sumodd = sum(odd[:oi+1])
            sumeven =  even[0]
        res = sumodd + sumeven
        res = res if res % D == 0 else -1

        while oi-1 >= 0 and ei+2 < len(even):
            sumodd -= (odd[oi]+odd[oi-1])
            sumeven += (even[ei+1]+even[ei+2])
            if (sumodd + sumeven) % D == 0:
                res = max(res,sumodd+sumeven)
            oi -= 2
            ei += 2
        print(res)

else:
    if len(odd) == 0:
        print(-1)
    else:
        oi,ei = 0,K-1
        sumodd = odd[0]
        sumeven =  sum(even[:ei+1])
        res = sumodd + sumeven
        res = res if res % D == 0 else -1

        while oi+2 < len(odd) and ei-2 >= 0:
            sumodd += (odd[oi+1]+odd[oi+2])
            sumeven -= (even[ei]+even[ei+1])
            if (sumodd + sumeven) % D == 0:
                res = max(res,sumodd+sumeven)
            oi += 2
            ei -= 2
        print(res)
