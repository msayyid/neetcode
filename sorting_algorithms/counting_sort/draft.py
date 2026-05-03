heights = [5, 100,2,3,4, 5, 5, 5, 55, 55, 1, 1, 1, 1]
count = [0] * 100
# count = {}
expected = [0] * len(heights)

for n in heights:
    # count[n] = count.get(n, 0) + 1
    count[n - 1] += 1
print(count)

i = 0 # i is to track the expected's index/order

for key in range(100):
    for _ in range(count[key]):
        expected[i] = key + 1
        i += 1
print(expected)