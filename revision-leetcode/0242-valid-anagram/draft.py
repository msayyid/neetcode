# s = "zlap"
# t = "kcqx"

s = "anagram"
t = "nagaram"

count = [0] * 26
print(count)
for i in range(len(s)):
    print(ord("z"))
    print(ord(s[i]))
    index = 26 - (ord("z") - ord(s[i])) - 1
    print(index)
    # break
    count[index] += 1

print(count)
