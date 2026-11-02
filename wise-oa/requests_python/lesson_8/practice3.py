# 1. Problem statement
# You are given a REST API endpoint containing paginated transaction records.

# Implement:
# def getAverageAmount(url: str) -> float:



# The function must return the average amount of transactions where:
# status == "COMPLETED"



# Transaction amounts are returned as formatted strings containing dollar signs, commas, and potentially decimal values.
# 2. API response format
# The API accepts a page query parameter and returns JSON containing page, total_pages, and data.
# Sample API responses

# Page 1


# GET /transactions?page=1
# {
#   "page": 1,
#   "total_pages": 3,
#   "data": [
#     {
#       "status": "COMPLETED",
#       "amount": "$1,200.50"
#     },
#     {
#       "status": "PENDING",
#       "amount": "$9,500.00"
#     },
#     {
#       "status": "COMPLETED",
#       "amount": "$800.25"
#     }
#   ]
# }


# 3. Requirements
# Your function must:
# 1. Send GET requests to retrieve all pages, starting from page 1.
# 2. Consider only transactions with status == "COMPLETED".
# 3. Convert formatted currency strings into numeric values, preserving decimal amounts.
# 4. Calculate the average of all matching transactions across every page.
# 5. Return the average as a float.
# 6. Return 0.0 if there are no COMPLETED transactions.
# 7. Assume all HTTP requests succeed and return valid JSON.
# 8. Avoid creating an additional list containing all matching transactions.
# 4. Expected result
# For the three example pages:

# EXPECTED RETURN VALUE
# 1250.5
# Average of the four COMPLETED transactions

# The PENDING and FAILED transactions must not contribute to the average.

import requests

def getAverageAmount(url: str) -> float:
    page = 1

    count = 0
    total = 0.0
    while True:
        params = {"page": page}
        response = requests.get(url, params=params)
        data = response.json()
        for item in data["data"]:
            if item["status"] == "COMPLETED":
                cur_amount = float(item["amount"].replace("$", "").replace(",", ""))
                count += 1
                total += cur_amount

        if page >= data["total_pages"]:
            break
        page += 1

    return (total / count) if count != 0 else total


