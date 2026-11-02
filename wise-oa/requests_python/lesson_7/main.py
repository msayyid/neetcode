# Lesson 7 - HTTP status code & error handling

# basics of error handling in requests library

# 1. HTTP status code
# response = requests.get(url)
# the server sends back an HTTP response, which includes a status code

# 200 - OK - request succeeded
# 201 - Created - resource successfully created
# 400 - Bad Request - invalid request
# 401 - Unauthorized - authentication required or invalid
# 403 - Forbidden - access denied
# 404 - Not Found - requested resource doesn't exist
# 429 - Too Many Requested - rate limit
# 500 - Internal Server Error

# inspect
# print(response.status_code)


# 2. What happens when a request fails?
# the server might return:
# 404 Not Found

# important detail!!!
# requests.get() does not automatically raise an exception just because the server 
# returned HTTP 404 or 500
# we can still inspect the response:
# print(repsonse.status_code) # 404

# if we want python to treat unsuccessful HTTP response as errors,
# we use raise_for_status()


# 3. response.raise_for_status()

# response = requests.get(url)
# response.raise_for_status()
# data = response.json()

# here's what happens:
# 200 OK - raise_for_status() does nothing, and execution continues to .json()
# 404 Not Found - raise_for_status() raises an HTTPError exception.

# so
# response.raise_for_status()
# essentially means: if the request returned an error status, raise an exception
# one distinction: it does not detect every possible failure. it won't
# tell you whether the server returned malformed JSON

# 4. handling exceptions
# import requests

# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()

#     data = response.json()

#     print(data)

# except requests.RequestException as e:
#     print("Request failed:", e)

# what is happening?
# 1. requsts.get() attempts to contact the server
# 2. timeout=10 prevents waiting indefinitely for an unresponsive request
# (it sets a connection/read inactivity timeout, not a strict total-duration limit)
# 3. raise_for_status() checks for HTTP error responses
# 4. .json() parses the response
# 5. if a relevant request-related exception occurs, the except block handles it


# ex 2 - handling API failures
import requests
def fetchUser(url:str) -> dict | None:
    try:
        response = requests.get(url, timeout=10) # timeout=10 prevents waiting indefinitely for an unresponsive request
        response.raise_for_status()
        data = response.json()
        return data

    except requests.RequestException:
        return None