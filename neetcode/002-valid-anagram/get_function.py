# user = {
#     "name": "Ali", 
#     "age": 30
# }

# print(user.get("name"))
# print(user.get("age"))
# # print(user.get("hobby")) # returns none (because key doesn't exist)
# # hobby = user["hobby"] # key error, as key doesnt' exist


# # default value
# # my_dict.get(key, default_value)
# # this means if key doesn't exist -> returns default value
# print(user.get("email", "not provided"))

# -----------------------------------
text = "aabca"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1 # this means, if ch key exists increment its value + 1 if doesn't assign 0 and incrmement by 1
    # If ch exists → get its current value and add 1
    # If ch does not exist → start from 0, then add 1
print(freq) 

# 7. When should you use get()?

# Use it when:
# You're not sure the key exists
# You want a safe fallback value
# You're building counters or accumulators