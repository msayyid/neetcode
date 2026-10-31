# Lesson 3 - filtering records

# filtering api records based on conditions
line = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

# data = [
#     {"id": 1, "status": "PAID", "amount": 500},
#     {"id": 2, "status": "PENDING", "amount": 1200},
#     {"id": 3, "status": "PAID", "amount": 700},
#     {"id": 4, "status": "FAILED", "amount": 300},
#     {"id": 5, "status": "PAID", "amount": 900}
# ]

# for transaction in data:
#     print(transaction)

# print only paid
# count = 0
# print(line)
# for transaction in data:
    # if transaction["status"] == "PAID":
        # count += 1
        # print(transaction)
# print(count)


# ex 1
transactions = [
    {"id": 1, "status": "PAID", "amount": 150},
    {"id": 2, "status": "FAILED", "amount": 800},
    {"id": 3, "status": "PAID", "amount": 250},
    {"id": 4, "status": "PENDING", "amount": 1000},
    {"id": 5, "status": "PAID", "amount": 600},
    {"id": 6, "status": "FAILED", "amount": 400}
]

# 1. counts how many transactions have status = "PAID"
# 2. calcualates the total amount of all paid transactions
# 3. finds the largest amount among paid transactions
print(line)
count = 0
total_of_paid = 0
largest_in_paid = None
for t in transactions:
    if t["status"] == "PAID":
        total_of_paid += t["amount"]
        count += 1
        if largest_in_paid is None or t["amount"] > largest_in_paid:
            largest_in_paid = t["amount"]
print(f"count: {count}")
print(f"total: {total_of_paid}")
print(f"maximum: {largest_in_paid}")

