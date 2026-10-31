# REST API - lesson 6 Pagination

# what is pagination?
# imagine an API contains 100 trasactions
# instead of returning all 100 at once, the server
# might return only 10 transactions per request

# that means we have:
# page 1 -> 10 transactions
# page 2 -> 10 transactions
# ...

# to retrieve all 100, we need to request every page
# this is called pagination


# 2. What does a paginated API response look like?
# Suppose we send:
# import requests
# url = "https://example.com/transactions"
# response = requests.get(url, params={"page": 1})
# data = response.json()



# The API might return:
# {
#     "page": 1,
#     "per_page": 2,
#     "total": 5,
#     "total_pages": 3,
#     "data": [
#         {"id": 1, "amount": 500},
#         {"id": 2, "amount": 700}
#     ]
# }

# breakdown
# page      = current page (1)
# per_page  = maximum records per page (2) # so this means one page can have max 2 records? it can have 1 or none as well? -- correct
# total     = total records across all pages (5) # so this means there overall 5 records in all the json
# total_pages = number of pages (3)  # and this is total pages
# data      = actual records on the current page

# api tells us there are 3 pages, but this response only contains the first page's records
# we need additional get requests to obtain the remaining records


# How do we request another page?
# to retrieve page 2:
# params = {"page": 2}
# response = requests.get(url, params=params)
# data = response.json()

# the pagination loop



# pagination exercise 1

# 5. Your turn — Pagination Exercise 1
# Before writing actual HTTP requests in a loop, I want to check 
# your understanding of how paginated data is structured.

# Imagine we've already fetched all three pages and stored their JSON responses in this list:
pages = [    
    {        
        "page": 1,        
        "total_pages": 3,        
        "data": [            
            {"name": "Alex", "amount": 500},            
            {"name": "Sara", "amount": 700}        
            ]    
    },    
    {        
        "page": 2,        
        "total_pages": 3,        
        "data": [            
            {"name": "John", "amount": 300},            
            {"name": "Emma", "amount": 900}        
            ]    
    },    
    {        
        "page": 3,        
        "total_pages": 3,        
        "data": 
        [            
            {"name": "James", "amount": 200}        
        ]    
    }
    ]



# Mini Exercise — Processing Multiple Pages
# Easy

# Write Python code to:
# 1. Iterate through all three pages.
# 2. Iterate through the records inside each page.
# 3. Calculate the sum of all transaction amounts across every page.
# 4. Print the final total.
# EXPECTED OUTPUT
# Total: 2600


# Constraint: Don't create a separate list containing all transactions. Use a running total.
# all_sum = 0
# for page in pages:
#     for item in page["data"]:
#         all_sum += item["amount"]
# print(all_sum)




# lesson 6 part 2: fetching pages automatically

# we need to send multiple get requests




def get_page(page):
    pages = {
        1: {
            "page": 1,
            "total_pages": 3,
            "data": [
                {"amount": 500},
                {"amount": 700}
            ]
        },
        2: {
            "page": 2,
            "total_pages": 3,
            "data": [
                {"amount": 300},
                {"amount": 900}
            ]
        },
        3: {
            "page": 3,
            "total_pages": 3,
            "data": [
                {"amount": 200}
            ]
        }
    }

    return pages[page]

# 1. Start with page = 1.
# 2. Retrieve each page using get_page(page).
# 3. Discover total_pages from the response.
# 4. Calculate the sum of all amounts across every page.
# 5. Stop after processing the last page.
# 6. Return the total amount.
def getTotalAmount() -> int:
    page = 1
    total = 0
    while True:
        data = get_page(page)
        # print(data)
        the_data = data["data"]
        # total += the_data["amount"]
        for item in the_data:
            total += item["amount"]

        # page += 1
        if page == data["total_pages"]:
            break
        page += 1
    # print(total)
    return total

print(getTotalAmount())



# Lesson 6 - part 3 Real HTTP pagination
# Problem: Total Transaction Amount Across All Pages
# Write a function:
# def getTotalAmount(url: str) -> int:



# The function receives an API endpoint URL.

# The API returns paginated transaction records.

# Assume the pages contain:
# API response preview

# Page 1
# Page 2
# Page 3


# GET /transactions?page=1
# {
#   "page": 1,
#   "total_pages": 3,
#   "data": [
#     {
#       "amount": 500
#     },
#     {
#       "amount": 700
#     }
#   ]
# }


# Requirements
# 1. Import requests.
# 2. Start from page 1.
# 3. Send a GET request using params={"page": page}.
# 4. Parse the JSON response.
# 5. Add all transaction amounts to a running total.
# 6. Continue until you've processed the last page.
# 7. Return the final total.
# Expected result: 2600
# Function template
import requests
def getTotalAmount(url: str) -> int:    
    page = 1    
    total = 0    
    # Your implementation here
    while True:
        params = {"page":page}
        response = requests.get(url, params=params)
        data = response.json()

        total_pages = data["total_pages"]

        for item in data["data"]:
            total += item["amount"]

        if page >= total_pages:
            break
        page += 1
    return total