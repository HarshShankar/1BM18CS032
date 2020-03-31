  
def find(n):
    arr = [[0 for h in range(n)]
           for b in range(n)]
    x = 0
    for i in range(n // 4):
        for j in range(n // 4):
            for h in range(4):
                for b in range(4):
                    arr[i * 4 + h][j * 4 + b] = x
                    x += 1
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()


n = int(input('Enter n: '))
find(n)
