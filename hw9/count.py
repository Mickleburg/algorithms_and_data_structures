st = input()

dct = dict()

for x in st:
    if x in dct:
        dct[x] += 1
    else:
        dct[x] = 1

k = 0
for val in dct.values():
    k = max(k, val)

print(k)
