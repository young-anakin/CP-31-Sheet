t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    ss = sorted(list(arr))
    if ss == arr:
        print("YES")
    elif k == 1:
        print("NO")
    else:
        print("YES")