
n, lst = input(), list(map(int, input().split()))
a = 0
for i in lst:
    lst[a] = int(i)
    a = a+1

print(max(lst)-min(lst))
