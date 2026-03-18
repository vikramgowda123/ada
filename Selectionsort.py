import random, time
import matplotlib.pyplot as plt

def selection_sort(a):
    for i in range(len(a)):
        m = i
        for j in range(i+1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]

n_values = [5000, 7000, 9000, 11000, 13000]
time_taken = []

for n in n_values:
    arr = [random.randint(1, 100000) for _ in range(n)]

    start = time.time()
    selection_sort(arr)
    end = time.time()

    time_taken.append(end - start)
    print("n =", n, "Time =", end - start)

plt.plot(n_values, time_taken, marker='o')
plt.xlabel("n")
plt.ylabel("time")
plt.title("Selection Sort")
plt.grid()
plt.show()
