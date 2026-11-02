# 1. Problem statement
# An online marketplace provides a REST API containing products from different categories.

# Implement a function that returns the name of the most expensive product in a specified category, 
# considering products across all API pages.

# Function signature
# def getMostExpensiveProduct(url: str, category: str) -> str:



# 2. API specification
# The API accepts one query parameter:

# - page — the page number, starting from 1.

# Important: The API does not support server-side category filtering. You must retrieve the pages 
# and identify matching products yourself.

# Each API response contains:
# {
#     "page": 1,
#     "total_pages": 3,
#     "data": [
#         {
#             "name": "MacBook Pro",
#             "category": "Electronics",
#             "price": "$2,499.99"
#         }
#     ]
# }


# Each product has three fields:
# Field	    Type	    Description
# name	    String	    Product name
# category	String	    Product category
# price	    String	    Formatted price, e.g. "$1,299.99"

# 3. Example API responses
# Sample API responses

# Page 1


# GET /products?page=1
# {
#   "page": 1,
#   "total_pages": 3,
#   "data": [
#     {
#       "name": "MacBook Pro",
#       "category": "Electronics",
#       "price": "$2,499.99"
#     },
#     {
#       "name": "Office Chair",
#       "category": "Furniture",
#       "price": "$399.50"
#     },
#     {
#       "name": "iPad Air",
#       "category": "Electronics",
#       "price": "$799.00"
#     }
#   ]
# }


# 4. Requirements
# Your function must:
# 1. Retrieve all available pages using HTTP GET requests.
# 2. Consider only products whose category exactly matches the provided category argument (case-sensitive).
# 3. Compare prices numerically, preserving decimal values.
# 4. Return the product name, not its price.
# 5. If multiple products share the highest price, return the product encountered first.
# 6. If no products match the requested category, return an empty string "".
# 7. Assume all requests succeed and return valid JSON with consistent pagination metadata.
# 8. Avoid storing all products in a separate list.
# 5. Expected result
# For:
# getMostExpensiveProduct(url, "Electronics")



# EXPECTED RETURN VALUE
# "Gaming PC"
# Price: $3,250.75

# The Gaming Laptop has the same price, but Gaming PC appears earlier in the API results.

# If you request "Clothing", the function should return "" because no matching products exist in the sample data.

import requests
def getMostExpensiveProduct(url: str, category: str) -> str:
    page = 1
    the_product = ""
    the_price = None
    while True:
        params = {"page": page}
        response = requests.get(url, params=params)
        data = response.json()
        for item in data["data"]:
            if item["category"].lower() == category.lower():
                cur_price = float(item["price"].replace("$", "").replace(",", ""))
                if the_price is None or cur_price > the_price:
                    the_price = cur_price
                    the_product = item["name"]
        if page == data["total_pages"]:
            break
        page += 1

    return the_product


