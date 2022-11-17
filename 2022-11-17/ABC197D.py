import math

N = int(input())
x0,y0 = map(int,input().split())
xh,yh = map(int,input().split())

xc,yc = (x0+xh)/2,(y0+yh)/2

cos = math.cos(2*math.pi/N)
sin = math.sin(2*math.pi/N)

x1 = (x0-xc)*cos - (y0-yc)*sin + xc
y1 = (x0-xc)*sin + (y0-yc)*cos + yc

print(x1,y1)
