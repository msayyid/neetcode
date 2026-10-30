# REST API Lesson 1 - First GET request

# we will be mainly doing:
# URL -> send GET Request -> receive response -> convert JSON into Python -> use normal dict/list operations

# import requests

# library requests makes HTTP requests easy

# requests.get() # get basically means give me some data
# we could request data with: 
# response = requsts.get("<url>")


# what is response?
# response = requests.get(url)
# response is not yet the actual list/dictionary we want to process

# it is an HTTP response object

# requests.get(url) -> response
# response contains several things, including:
# response.status_code
# response.json()


# response.status_code
# when we request something from a server, the server gives you a status code



# response.json()

# if we receive this
# {
#     "name": "Alex",
#     "age": 24,
#     "country": "UK"
# }
# we do
# data = response.json()

# now data becomes an ordinary Python dict

# we can do:
# print(data["name"])

# JSON from API -> response.json() -> normal Python dict/list
# after this, we can forget that we are doing something mysterious with REST
# it will mostly be solving a Python problem

# complete tiny example:

# 5. Complete tiny example
# Suppose:
# url = "https://example.com/user/1"


# # And imagine that endpoint returns:
# {
#     "id": 1,
#     "name": "Sara",
#     "balance": 500
# }

# # Our Python would look like:
# import requests
# url = "https://example.com/user/1"
# response = requests.get(url)
# print(response.status_code)
# data = response.json()
# print(data)
# print(data["name"])
# print(data["balance"])


# Conceptually:
# requests.get(url)
#         ↓
#       response
#         ↓
#       response.json()
#         ↓
#       data
#         ↓
#   Python dictionary

# So this:
# response


# and this:
# data


# are not the same thing.
# response
# HTTP response object:
# response.status_coderesponse.json()


# data
# The JSON converted into Python:
# data["name"]data["balance"]



# when we are unsure we can do:
# data = response.json()
# print(type(data))
# print(data)


# memorize this translation
# API endpoint
# -> requests.get(url)

# response status
# -> response.status_code

# JSON response
# -> response.json()

# response.json()
# -> normal Python dict/list


# exercise

# url = "https://example.com/student/7"
# returns:
# {
#     "id": 7,
#     "name": "Avery",
#     "score": 92
# }

# import requests
# url = "https://example.com/student/7"

# # 1. send a get request
# response = requests.get(url) 
# # requests.get(url) does not directly return a JSON dict
# # it returns a Response object
# # it contains things like:
# # response.status_code
# # response.text # response body as text
# # response.json() # parses the body as JSON and returns Python data

# # 2. print the HTTP status code
# print(response.status_code)

# # 3. convert the JSON response into python
# data = response.json()

# # 4. print the student's name
# print(data["name"])

# # 5. print the student's score
# print(data["score"])


# try a real API
import requests
url = "https://jsonplaceholder.typicode.com/users/1"
# response = requests.get(url)
# print(response.status_code)
# print(response.text)
# print("--------")
# print(type(response.text))


# data = response.json()
# print(data)
# print(type(data))
line = "#######################################################"

# next exercise

# modify the code to print
# 1. the user's name
response = requests.get(url)
data = response.json()
print(data["name"])

# 2. email
print(data["email"])


# 3. city
print(line)
print(data["address"]["city"])
# this is one way 
# cleaner way:
city = data["address"]["city"]
print(city)
# i m not sure if it was cleaner honestly

# 4. type of data using type()
print()
print(line)
print(type(data))

# for the question, if the json contains address' value as a dict
# we access the value associated with the "address" key in the outer dict,
# which is itself another dictionary. then we access the value associated with
# the "city" key in that inner dictionary

