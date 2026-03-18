import random, time
import matplotlib.pyplot as plt

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    l = merge_sort(a[:mid])
    r = merge_sort(a[mid:])
    return sorted(l + r)   # simplest merge

n_values = [5000, 7000, 9000, 11000, 13000]
time_taken = []

for n in n_values:
    arr = [random.randint(1, 100000) for _ in range(n)]

    start = time.time()
    arr = merge_sort(arr)
    end = time.time()

    time_taken.append(end - start)
    print("n =", n, "Time =", end - start)

plt.plot(n_values, time_taken, marker='o')
plt.xlabel("n")
plt.ylabel("time")
plt.title("Merge Sort")
plt.grid()
plt.show()
