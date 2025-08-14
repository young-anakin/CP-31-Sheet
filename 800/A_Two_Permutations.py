t = int(input())
for _ in range(t):
    n, a, b= list(map(int, input().split(" ")))
    
    mx = min(n, a+b)

    remaining = n - mx
    if (n == a == b) or remaining > 1:
        print("Yes")
    else:
        print("No")
    # print(remaining)
