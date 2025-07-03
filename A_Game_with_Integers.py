t = int(input())

for _ in range(t):
    n = int(input())
    if not (n-1)%3 or not(n+1) %3:
        print("First")
    else:
        print("Second")