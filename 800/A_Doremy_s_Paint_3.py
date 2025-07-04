t = int(input())
from collections import Counter
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    cp = Counter(arr)
    ss = list(set(arr))
    if len(cp) == 2:
        if abs(cp[ss[0]] - cp[ss[1]]) <= 1:
            print("Yes")
        else:
            print("No")
    elif len(cp) == 1:
        print("Yes")
    else:
        print("No")
    