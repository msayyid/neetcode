# Practice 1 — Highest Transaction
# Easy–Medium
# Suggested target: 15–20 minutes

# Problem statement
# You are given a REST API endpoint containing transaction records across multiple pages.

# Your task is to implement a function that returns the name of the user who made the largest completed transaction.

# Function signature
# def getHighestTransactionUser(url: str) -> str:



# API response format
# The API accepts a page query parameter and returns paginated JSON.
# Example API responses

# Page 1


# GET /transactions?page=1
# {
#   "page": 1,
#   "total_pages": 3,
#   "data": [
#     {
#       "user": "Alex",
#       "status": "COMPLETED",
#       "amount": "$1,250"
#     },
#     {
#       "user": "Sara",
#       "status": "PENDING",
#       "amount": "$9,500"
#     },
#     {
#       "user": "John",
#       "status": "COMPLETED",
#       "amount": "$3,400"
#     }
#   ]
# }


# Requirements
# 1. Fetch all pages, starting from page 1.
# 2. Consider only transactions where status == "COMPLETED".
# 3. Amounts are formatted strings such as "$1,250".
# 4. Return the user's name, not the amount.
# 5. Assume at least one completed transaction exists.
# 6. If multiple users have transactions with the same maximum amount, 
# return the name of the user encountered first (page order, then record order).
# 7. Assume all HTTP responses are successful and contain valid JSON.

# Expected result
# Emma
# Largest completed transaction: $6,800

import requests
def getHighestTransactionUser(url: str) -> str:
    page = 1
    largest_amount = None
    cur_user = None
    while True:
        params = {"page": page}
        response = requests.get(url, params=params)
        data = response.json()
        total_pages = data["total_pages"]
        for item in data["data"]:
            if item["status"] == "COMPLETED":
                cur_amount = int(item["amount"].replace("$", "").replace(",", ""))
                if largest_amount is None or cur_amount > largest_amount:
                    largest_amount = cur_amount
                    cur_user = item["user"]
        if page == total_pages:
            break
        page += 1
    return cur_user



# a cleaned up version:

# import requests

# def getHighestTransactionUser(url: str) -> str:
#     page = 1
#     largest_amount = None
#     highest_user = None

#     while True:
#         response = requests.get(url, params={"page": page})
#         data = response.json()

#         for item in data["data"]:
#             if item["status"] == "COMPLETED":
#                 amount = int(
#                     item["amount"].replace("$", "").replace(",", "")
#                 )

#                 if largest_amount is None or amount > largest_amount:
#                     largest_amount = amount
#                     highest_user = item["user"]

#         if page == data["total_pages"]:
#             break

#         page += 1

#     return highest_user
    
        
        