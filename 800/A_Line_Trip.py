t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))

    mx = arr[0]

    for i in range(1, len(arr)):
        mx = max(mx, arr[i] - arr[i-1])
    
    mx = max(mx, 2 * abs(x - arr[-1]))

    print(mx)