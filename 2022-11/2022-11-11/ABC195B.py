A,B,W = map(int,input().split())

W *= 1000
R = W // A 
L = W // B 

minres = 10**10
maxres = 0

for i in range(L,R+1):
    if A*i <= W <= B*i:
        minres = min(minres,i)
        maxres = max(maxres,i)

if maxres == 0:
    print("UNSATISFIABLE")
else:
    print(minres,maxres)
