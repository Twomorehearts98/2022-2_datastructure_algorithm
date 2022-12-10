
def enqueue(l, num):
    l[num % 10].append(num)

def enqueue2(l, num):
    for i in num:
        l[int(i // 10)].append(i)

a = [[] for i in range(10)]
b = [[] for i in range(10)]

lst = list(map(int, input().split()))

for i in lst:
    enqueue(a, i)
print(a)
print(b)
for i in a:
    if len(i)>0:
        enqueue2(b, i)
print(b)