# 1. Problem statement
# You are given a REST API containing users and their transaction counts.

# Implement a function that returns the name of the user with the highest number of transactions in a given country.

# Function signature
# def getTopUserByCountry(url: str, country: str) -> str:



# The API accepts two query parameters:
# - country — filters users by country.
# - page — specifies which page to retrieve.
# For example, to retrieve UK users on page 2:
# GET /users?country=UK&page=2


# 2. API response format
# The endpoint returns paginated JSON. Here are three sample responses when country="UK".
# Example API responses

# Page 1Page 2Page 3


# GET /users?country=UK&page=1
# {
#   "page": 1,
#   "total_pages": 3,
#   "data": [
#     {
#       "name": "Alex",
#       "country": "UK",
#       "transactions": 12
#     },
#     {
#       "name": "Sara",
#       "country": "UK",
#       "transactions": 25
#     }
#   ]
# }


# Notice that each record contains:
# Field	Meaning
# name	User's name
# country	User's country
# transactions	Number of transactions made by the user

# The transactions field is already an integer. You don't need currency parsing.
# 3. Requirements
# Your function must:
# 1. Fetch all pages using the country and page query parameters.
# 2. Find the user with the highest transactions value.
# 3. Return that user's name, not the number of transactions.
# 4. If two users have the same highest transaction count, return the first encountered.
# 5. If no users are returned, return an empty string "".
# 6. Assume all HTTP requests succeed, return valid JSON, and the API correctly applies the country filter.
# 7. Avoid creating an additional list containing users from every page.

# 4. Expected result
# For the example responses:
# RETURN VALUE
# "Emma"
# 42 transactions — the highest across all three pages

import requests

def getTopUserByCountry(url: str, country: str) -> str:
    page = 1
    highest_transactions = None
    highest_user = ""
    while True:
        params = {
            "country": country, 
            "page": page
        }
        response = requests.get(url, params=params)
        data = response.json() # question, since we passed country as a param, this means we will onlny reaceive data with the country = UK no?

        for item in data["data"]:
            if item["country"] == country:
                # a thought, since we have country in the parameters, i think we do nto really need to check if country corresponds to country do we?
                # but i think this will work fine as well i think, because it willliterally allow all the transactions we have

                cur_transactions = item["transactions"]
                if highest_transactions is None or cur_transactions > highest_transactions:
                    highest_transactions = cur_transactions
                    highest_user = item["name"]
        if page >= data["total_pages"]:
            break
        page += 1
    

    return highest_user

