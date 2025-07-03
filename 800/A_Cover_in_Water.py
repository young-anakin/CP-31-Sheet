t = int(input())
for _ in range(t):
    n = int(input())
    arr = input()

    i = 0
    j = 2
    found = False
    while j < n:
        if arr[i] == arr[i+1] == arr[i+2] == ".":
            found = True
            break
            
        i +=1
        j +=1    
    
    if found:
        print(2)
    else:
        print(arr.count("."))
    # print(found)


