t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split(" ")))
    first = input()
    second = input()

    if second in first:
        print(0)
        continue
    
    cp = 0
    fl = True
    for _ in range(10):
        first += first
        cp +=1
        if second in first:
            print(cp)
            fl = False
            break
        # if len(first) > len(second):
        #     break
    if fl:
        print(-1)