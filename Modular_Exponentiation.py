a,b,n = map(int,input().split())
r = 1
for i in range(0,b-1):
    r = (r * a)%n
print(r)
