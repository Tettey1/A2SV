
t = int(input())

def solve():
    n = int(input())
    b = list(map(int, input().split()))
    # a0 = b[0]
    # an = b[-1]
    a = [0]*n
    
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1,n-1):
        a[i]=min(b[i-1],b[i])
    print(*a)
        

for _ in range(t):
    solve()