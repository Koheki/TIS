A,B = map(int,input().split())

g = int((A/(2*B))**(2/3))+1
print(B*(g-1)+A/(g**0.5))
