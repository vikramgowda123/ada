def find(p, x):
    return x if p[x] == x else find(p, p[x])

edges = []
e = int(input("Enter number of edges: "))

print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = input().split()
    edges.append((int(w), u, v))

p = {}
cost = 0

edges.sort()

for w, u, v in edges:
    if u not in p: p[u] = u
    if v not in p: p[v] = v

    a = find(p, u)
    b = find(p, v)

    if a != b:
        p[a] = b
        cost += w
        print(u, "-", v, "=", w)

print("Cost =", cost)
