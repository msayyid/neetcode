# words = ["Python", "is", "great"]
# result = " ".join(words)
# print(result)

# items = ["apple", "banana", "orange"]
# result = "-".join(items)
# print(result)


# names = ["Ali", "John", "Sara", "Mike"]
# # Ali, John, Sara, Mike
# final_names = ", ".join(names)
# print(final_names)

# words = ["Python", "Java", "C++"]
# # Python | Java | C++
# result = " | ".join(words)
# print(result)



# words = ["Learning", "Python", "is", "very", "powerful"]
# # Learning Python is very powerful.
# result = " ".join(words) + "."
# print(result)

# integers
# numbers = [1, 2, 3, 4, 5]
# # result = "-".join(str(number) for number in numbers)
# result = "-".join(map(str, numbers))
# print(result)

# text = "python is powerful"
# # p-y-t-h-o-n- -i-s- -p-o-w-e-r-f-u-l
# result = "-".join(c for c in text)
# print(result)

words = ["apple", "banana", "cherry"]

result = "-".join(words) + "!"
print(result)