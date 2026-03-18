n = int(input("Enter number of vertices: "))
cost = [list(map(int, input().split())) for _ in range(n)]
vis = [False] * n
vis[0] = True
total = 0

for _ in range(n - 1):
    m, x, y = 999, 0, 0
    for i in range(n):
        for j in range(n):
            if vis[i] and not vis[j] and 0 < cost[i][j] < m:
                m, x, y = cost[i][j], i, j
    print(x, "-", y, "=", m)
    total += m
    vis[y] = True

print("Cost =", total)
