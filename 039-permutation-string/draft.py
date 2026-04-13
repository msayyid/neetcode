s1 = "abc"
s2 = "lecabee"
k = len(s1)

count1 = [0] * 26
for c in s1:
    count1[ord(c) - ord("a")] += 1

count2 = [0] * 26
print(count2)
for c in s2[:k]:
    count2[ord(c) - ord("a")] += 1
print(count2)
print("this is count1 - \n", count1)

for i in range(len(s2) - k + 1):
    count2[i] -= 1
    count2[i + k] += 1
    print(count2)