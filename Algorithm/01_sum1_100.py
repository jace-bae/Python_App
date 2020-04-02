# sum 1 ~ 100

# 1. 앞의 결과를 기억하여 for문으로 구하는 방법
def sum_num(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s
print(sum_num(100))


# 2. 일반화된 수학 공식(n(n+1)
def sum_gop(n):
    return n * (n+1)//2
print(sum_gop(100))
