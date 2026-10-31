# Next: Paginated Filtered Max Amount
# Now it's time to combine everything you've learned so far.
# Wise-style REST Practice 2
# Medium

# Implement:
import requests
def getMaxAmount(url: str) -> int:    
    # Your solution
    page = 1
    largest_amount = None
    while True:
        params = {"page":page}
        response = requests.get(url, params=params)
        data = response.json()
        total_pages = data["total_pages"]
        for transaction in data["data"]:
            if transaction["status"] == "PAID":
                cur_amount = int(transaction["amount"].replace("$", "").replace(",",""))
                if largest_amount is None or largest_amount < cur_amount:
                    largest_amount = cur_amount

        if page == total_pages:
            break
        page += 1
    return largest_amount




# The API accepts a page query parameter and returns responses like:
# {
#   "page": 1,
#   "total_pages": 3,
#   "data": [
#     {"status": "PAID", "amount": "$1,200"},
#     {"status": "PENDING", "amount": "$9,500"},
#     {"status": "PAID", "amount": "$3,400"}
#   ]
# }


# Requirements:
# 1. Fetch every page, beginning at page 1.
# 2. Consider only records with status == "PAID".
# 3. Convert formatted money strings into integers.
# 4. Find and return the largest PAID amount across all pages.
# 5. Don't store all transactions in an additional list.
# Assume at least one PAID transaction exists and the API returns valid responses.