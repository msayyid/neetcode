# REST API — Practice 1: Filtered Max Amount

# Problem statement
# You are given a URL pointing to a REST API endpoint containing transaction records.

# Your task is to write a function that:
# 1. Sends an HTTP GET request to the endpoint.
# 2. Reads the JSON response.
# 3. Considers only transactions where status == "PAID".
# 4. Returns the largest transaction amount among those records.

# API response format
# The endpoint returns a JSON list of dictionaries.

# Example:
# [
#     {
#         "id": 1,
#         "status": "PAID",
#         "amount": "$1,200"
#     },
#     {
#         "id": 2,
#         "status": "PENDING",
#         "amount": "$9,500"
#     },
#     {
#         "id": 3,
#         "status": "PAID",
#         "amount": "$3,400"
#     },
#     {
#         "id": 4,
#         "status": "FAILED",
#         "amount": "$12,000"
#     },
#     {
#         "id": 5,
#         "status": "PAID",
#         "amount": "$2,750"
#     }
# ]


# Expected output
# RETURN VALUE
# 3400
# The largest amount among PAID transactions

# Notice that the transaction containing $12,000 must be ignored because its status is FAILED.
# Constraints and assumptions
# - At least one PAID transaction exists.
# - All amounts are non-negative whole-dollar values.
# - Amounts have the format "$1,234" or "$500".
# - The API returns a JSON list, not a paginated dictionary.
# - Assume the request succeeds and the response contains valid JSON.
# - Return an integer, not a formatted string.

data = [
    {"id": 1, "status": "PAID", "amount": "$1,200"},
    {"id": 2, "status": "PENDING", "amount": "$9,500"},
    {"id": 3, "status": "PAID", "amount": "$3,400"},
    {"id": 4, "status": "FAILED", "amount": "$12,000"},
    {"id": 5, "status": "PAID", "amount": "$2,750"}
]

# Your task
# Implement:
import requests
def getMaxAmount(url: str) -> int:    
    # Your implementation here
    # 1. send http get request
    # response = requests.get(url)

    # 2. read the json response
    # data = response.json() # this is what i would have done if it were a real url

    # 3. consider only PAID
    largest_tran = None
    for transaction in data:
        if transaction["status"] == "PAID":
            current = int(transaction["amount"].replace("$", "").replace(",", ""))
            if largest_tran is None or largest_tran < current:
                largest_tran = current
    return largest_tran

print(getMaxAmount("example"))