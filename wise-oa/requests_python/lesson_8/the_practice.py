# # REST API: Average Heartbeat

# Given the name of a marathon and a gender, identify the fastest runner of that gender in the marathon.

# Use HTTP GET requests to query a marathon runner database at the URL:

# ```text
# https://jsonmock.hackerrank.com/api/marathon
# ```

# The results are paginated and can be accessed by appending `&page={num}` to the query string, where `{num}` is the page number.

# To filter the query by specific fields, append `{fieldname}={value}` to the URL.

# For example:

# ```text
# https://jsonmock.hackerrank.com/api/marathon?sex=female&page=2
# ```

# This returns the second page of the filtered list of female runners.

# ## API Response Structure

# The query response from the API includes these fields:

# | Field | Description |
# |---|---|
# | `page` | The current page |
# | `per_page` | The maximum results per page |
# | `total` | The total number of records |
# | `total_pages` | The total number of pages for the query |
# | `data` | An array of JSON objects containing runner information |

# Each object in the `data` field includes the following:

# - `name`: The name of the runner
# - `marathon_name`: The name of the marathon
# - `sex`: The sex of the marathon runner
# - `avgheartbeat`: The average heart rate of the runner during the marathon
# - Other details not relevant to this question

# ### Example JSON Record

# The following is an example record from the API:

# ```json
# {
#     "name": "Gene Zboncak-Hansen",
#     "sex": "female",
#     "id": "867b0d8c-2b23-4e7e-aabc-5747f67969f1",
#     "age": 99,
#     "top_speed": 13.42,
#     "bottom_speed": 4.75,
#     "average_speed": 7.01,
#     "avgheartbeat": 114,
#     "distance_run": 18.066,
#     "marathon_name": "Sunset Serenity Marathon",
#     "country": "Falkland Islands (Malvinas)",
#     "number_of_participants": 40,
#     "personal_best_time": 2914,
#     "stops_taken": 5,
#     "position": 40
# }
# ```

# ## Task

# Return the **average heart rate of the runners meeting the criteria, rounded down to the nearest integer**.

# ## Function Description

# Complete the function `averageHeartBeat` in the editor with the following parameters:

# ```python
# def averageHeartBeat(marathon: str, sex: str) -> int:
# ```

# ### Parameters

# - `string marathon`: The marathon name
# - `string sex`: The sex to filter the runners by

# ### Returns

# - `int`: The average heart rate of the runners of the given sex in the specified marathon

# **Note:** Please review the header in the code stub to see available libraries for API requests in the selected language. Required libraries can be imported to solve the question. Check the full list of supported libraries at:

# https://www.hackerrank.com/environment

# ---

# ## Input Format For Custom Testing

# ## Sample Case 0

# ### Sample Input

# ```text
# Cityscape Marathon
# female
# ```

# ### Sample Output

# ```text
# 120
# ```

# ### Explanation

# The average heart rate of 25 female participants in the Cityscape Marathon comes out to be 120.4, which, when rounded down, is 120.

# ---


import requests
import math
url = "https://jsonmock.hackerrank.com/api/marathon"
def averageHeartBeat(marathon: str, sex: str) -> int:

    page = 1
    count = 0
    total_hb = 0

    while True:

        params = {"page":page, "marathon_name":marathon, "sex":sex}
        response = requests.get(url, params=params)
        data = response.json()

        for item in data["data"]:
            if item["marathon_name"] == marathon and item["sex"] == sex:
                count += 1
                total_hb += item["avgheartbeat"]

        if page >= data["total_pages"]:
            break

        page += 1

    return math.floor(total_hb / count)

# print(averageHeartBeat("Cityscape Marathon", "female"))
