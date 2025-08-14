t = int(input())
for _ in range(t):
    n = int(input())

    sm = 0
    start = 0
    while start < n:
        if start < 10:
            sm +=1
            start +=1
        elif len(str(start)) == 2 and start + 10 <= n:
            sm +=1
            start +=10
        elif len(str(start)) == 3 and start + 100 <= n:
            sm +=1
            start += 100
        elif len(str(start)) == 4 and start + 1000 <= n:
            sm +=1
            start += 1000
        elif len(str(start)) == 5 and start + 10000 <= n:
            sm +=1
            start += 10000
        elif len(str(start)) == 6 and start + 100000 <= n:
            sm +=1
            start += 100000
        elif len(str(start)) == 7 and start + 1000000 <= n:
            sm +=1
            start += 1000000

        elif len(str(start)) == 8 and start + 10000000 <= n:
            sm +=1
            start += 10000000

        elif len(str(start)) == 9 and start + 100000000 <= n:
            sm +=1
            start += 100000000
        else:
            break
    
    print(sm)