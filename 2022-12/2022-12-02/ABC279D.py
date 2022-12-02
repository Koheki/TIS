import math

A,B = map(int,input().split())

g = (A/(2*B))**(2/3)
g1,g2 = math.ceil(g),math.floor(g)

if g1 == 0 or g2 == 0:
    print(A)
else:
    print(min(B*(g1-1)+A/math.sqrt(g1),B*(g2-1)+A/math.sqrt(g2)))
