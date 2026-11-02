# 1. Problem statement
# You are given a REST API endpoint containing customer records across multiple pages.

# Your task is to count how many customers satisfy both of these conditions:
# - Their country is "UK".
# - Their status is "ACTIVE".
# Function signature
# def countActiveCustomers(url: str) -> int:



# 2. API response format
# The endpoint accepts a page query parameter and returns paginated JSON.

# For this exercise, the API does not support server-side filtering by country or status. You'll need to examine the returned records.
# Example API responses

# Page 1


# GET /customers?page=1
# {
#   "page": 1,
#   "total_pages": 3,
#   "data": [
#     {
#       "id": 1,
#       "name": "Alex",
#       "country": "UK",
#       "status": "ACTIVE"
#     },
#     {
#       "id": 2,
#       "name": "Sara",
#       "country": "UK",
#       "status": "INACTIVE"
#     },
#     {
#       "id": 3,
#       "name": "John",
#       "country": "US",
#       "status": "ACTIVE"
#     }
#   ]
# }


# 3. Requirements
# Your function must:
# 1. Send GET requests to retrieve every page, starting from page 1.
# 2. Examine every customer record in each page's data list.
# 3. Count customers whose country == "UK" and status == "ACTIVE".
# 4. Return the total count across all pages.
# 5. Return 0 if there are no matching customers.
# 6. Assume requests succeed, the JSON is valid, and pagination metadata is consistent.
# 7. Avoid storing customer records from multiple pages in an additional list.

# Notice that the function should return an integer, not a list of customers.

# 4. Expected result
# EXPECTED RETURN VALUE
# 4
# Four customers satisfy both conditions across the three pages.

# Page 1	Alex
# Page 2	Emma, Sophie
# Page 3	Olivia

import requests
def countActiveCustomers(url: str) -> int:
    page = 1
    count = 0
    while True:
        params = {"page":page}
        response = requests.get(url, params=params)
        data = response.json()
        for item in data["data"]:
            if item["country"] == "UK" and item["status"] == "ACTIVE":
                count += 1

        if page >= data["total_pages"]:
            break
        page += 1

    return count