
t = int(input())


def solve(n,k,p):
    count=0
    for i in range(n):
        if (p[i]-i-1)%k==0:
            continue
        count+=1
    
    
    if count==0:
        print(0)
    elif count<=2:
        print(1)
    else:
        print(-1)

	

       
for _ in range(t):
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    solve(n,k,p)