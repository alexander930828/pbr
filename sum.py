# 단순 더하기

def sum(s):
    a = 0
    for i in range(1, s+1):
        a = a + i
    return a

print(sum(10))
print(sum(100))

# 등차 수열

def sum_1(s):
    a = 0
    a = s * (s + 1) // 2
    return a

print(sum_1(10))
print(sum_1(100))

