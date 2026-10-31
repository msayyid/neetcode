# REST API - Lesson 5 - Query Parameters

# How to request specific data from an API, rather than retrieving everything


# The URL might look like:
# https://example.com/transactions?country=UK&page=2

# Let's break it down.
# Anatomy of a URL with query parameters
# https://example.com/transactions

# Base URL — the API endpoint

# ?country=UK

# First parameter: country is UK

# &page=2

# Second parameter: page is 2


# There are three important symbols:
# Symbol	Meaning
# ?	        Starts the query parameters
# =	        Assigns a value to a parameter
# &	        Separates multiple parameters

# For example:
# ?status=PAID&page=3


# Means we're requesting records with the status parameter set to PAID, 
# on page 3, assuming the API supports those parameters.

# Important: The API decides which parameters it accepts. 
# Adding ?country=UK doesn't automatically make every API filter by country.



# 2. Approach 1 — Build the URL yourself
# Suppose HackerRank gives you:
# url = "https://example.com/transactions"
# country = "UK"
# page = 2



# You can construct the complete URL using an f-string:
# full_url = f"{url}?country={country}&page={page}"
# response = requests.get(full_url)
# data = response.json()



# That's perfectly valid.

# The generated URL is:
# https://example.com/transactions?country=UK&page=2


# Simple, right?

# However, manually building URLs can become error-prone when values contain spaces 
# or special characters, or when a URL already contains query parameters.


# 3. approach 2 - use params (recommended)
# requests library can build query parameters for us

# import requests
# url = "https://example.com/transactions"
# params = {
#     "country": "UK",
#     "page": 2
# }

# response = requests.get(url, params=params)
# data = response.json()

# this automatically builds the query string
# the two approaches send equivalent requests for this example



# mini exercise
# ex 1
import requests
url = "https://jsonplaceholder.typicode.com/posts"

# Write a Python program that:
# 1. Sends a GET request with the query parameter userId=2.
# 2. Converts the JSON response into Python data.
# 3. Prints the final request URL using response.url.
# 4. Prints the number of posts returned.
# 5. Prints the title of every returned post.
# Use the params dictionary approach, not manually constructed URLs, for this exercise.
params = {
    "userId":2
}
# i have a question in here, so the userId, i mean we will be given this right? 
# i mean how the keys and values are? i mean we cannot know what json we will get
# we don't really know its content, unless we print the content? it could be
# something like user_id or just u_id, i m not sure i made sense

### answered
# we know it from the API documentation or the Hackerrank problem statement
response = requests.get(url, params=params)
print(response.url)
print()
print()
print(response.text)
print()
print()
data = response.json()

print(f"Number of posts returned: {len(data)}")

print()
print()

for item in data:
    print(item["title"])
