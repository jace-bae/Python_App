def find_max(a):
    n = len(a)
    max_n = a[0]
    for i in range(1, n):
        if a[i] > max_n:
            max_n = a[i]
    return max_n

v = [10, 2, 18, 23, 59, 24, 33, 62]
print(find_max(v))