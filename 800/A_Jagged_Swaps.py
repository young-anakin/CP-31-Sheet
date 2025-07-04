t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))

    if arr[0] == 1 or  sorted(list(arr)) == arr:
        print("YES")
    else:
        print("NO")