# lesson 4: parsing formatted currency

# transactions = [
#     {"status": "PAID", "amount": "$1,200"},
#     {"status": "PENDING", "amount": "$9,500"},
#     {"status": "PAID", "amount": "$3,400"}
# ]

# amount = "$1,234"
# cleaned = amount.replace("$", "").replace(",", "")
# number = int(cleaned)
# # converting a floating number to int will raise an error

# print(number)


# ex

transactions = [
    {"id": 1, "amount": "$1,250"},
    {"id": 2, "amount": "$3,400"},
    {"id": 3, "amount": "$850"},
    {"id": 4, "amount": "$12,500"}
]

# Your tasks:
# 1. Convert each formatted amount into an integer.
# 2. Calculate the total amount of all transactions.
# 3. Find the largest transaction amount.
# 4. Do everything using a single loop without storing an additional list.
# EXPECTED OUTPUT
# Total: 18000
# Maximum: 12500
total_amount = 0
largest_amount = None
for t in transactions:
    cur_amount = int(t["amount"].replace("$", "").replace(",", ""))
    total_amount += cur_amount
    if largest_amount is None or cur_amount > largest_amount:
        largest_amount = cur_amount
print(f"Total: {total_amount}")
print(f"Maximum: {largest_amount}")
