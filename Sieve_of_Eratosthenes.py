n = int(input())
arr = [0 for i in range(n+1)]
p = 2
while (p * p <= n):
 if (arr[p] == 0):
     for i in range(p * 2, n+1, p):
         arr[i] = False
 p =p+ 1
 for p in range(2, n):
     if arr[p]:
print (p)
