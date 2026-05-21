from collections import Counter
from math import ceil
from typing import List


def calculateMinShipments(warehouses: List[int]) -> int:
    count = Counter(warehouses)
    total = 0
    n = len(warehouses)

    max_freq = max(count.values())
    others = n - max_freq

    print(count)
    print(max_freq)
    print(others)
    if max_freq > n - max_freq:
        res = others + max_freq - others
        return res
    else:
        return ceil(n / 2)

print(calculateMinShipments([1, 3, 1, 2]))
print(calculateMinShipments([1, 1, 1, 2, 3]))
print(calculateMinShipments([5, 5, 5, 5]))
print(calculateMinShipments([1, 2, 3, 4]))
# print(result)


from collections import Counter
from math import ceil
from typing import List

def calculateMinShipments(warehouses: List[int]) -> int:
    count = Counter(warehouses)
    n = len(warehouses)

    max_freq = max(count.values())
    others = n - max_freq

    if max_freq > others:
        return max_freq
    else:
        return ceil(n / 2)