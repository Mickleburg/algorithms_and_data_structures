N = int(input())
lst = list(map(int, input().split()))

dct = dict()

for x in lst:
    if x in dct:
        dct[x] += 1
    else:
        dct[x] = 1

for key, val in dct.items():
    if val > N / 2:
        print(key)
        break
else:
    print(-1)
