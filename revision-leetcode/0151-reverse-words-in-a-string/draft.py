
# s = "the sky is blue"
# words = []
# word = ""
# for i in range(len(s)):
#     if s[i] != " ":
#         word += s[i]
#     else:
#         if word:
#             words.append(word)
#             word = ""
# if word:
#     words.append(word)
# print(words)
# left = 0
# right = len(words) - 1
# while left < right:
#     words[left], words[right] = words[right], words[left]
#     left += 1
#     right -= 1
# print(words)
# s = " ".join(words)
# print(s)

s = "the sky is blue"
s[0] = s[4] # error strings are immutable
print(s)