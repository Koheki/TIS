N = int(input())

n = 0

for s12 in range(1,10):
    for s3 in range(10):
        for s4 in range(10):
            for s56 in range(10):
                for s79 in range(10):
                    for s8 in range(10):
                        n += 1
                        if n == N:
                            ans = str(s12)+str(s12)+str(s3)+str(s4)+str(s56)+str(s56)+str(s79)+str(s8)+str(s79)
                            print(ans)
                            exit()