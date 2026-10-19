"""
1. JSON Value Differences
Problem
You are given two strings json1 and json2, each representing a flat JSON object.
Each JSON object contains string keys and string values.
Return a list containing every key that:
appears in both JSON objects, and
has different values in the two objects.
Keys that appear in only one object should be ignored.
Return the result in lexicographical order.
Example 1
Input:
json1 = '{"name":"Alex","age":"25","city":"New York"}'
json2 = '{"name":"Alex","age":"30","city":"Los Angeles","country":"USA"}'

Output:
["age", "city"]
Explanation
"name" appears in both objects and has the same value:
Alex == Alex
"age" appears in both but:
25 != 30
"city" appears in both but:
New York != Los Angeles
"country" appears only in json2, so it is ignored.
Therefore:
["age", "city"]
Example 2
Input:
json1 = '{"hacker":"rank","input":"output"}'
json2 = '{"hacker":"ranked","input":"wrong"}'

Output:
["hacker", "input"]
Example 3
Input:
json1 = '{"a":"1","b":"2"}'
json2 = '{"a":"1","b":"2","c":"3"}'

Output:
[]
Constraints
1 <= len(json1), len(json2) <= 100000

All keys are unique within each JSON object.

Both strings represent valid flat JSON objects.

Keys and values are strings.

The objects do not contain nested JSON objects or arrays.
Function
def findDifferentValues(json1: str, json2: str) -> list[str]:
Pattern
JSON parsing + Hash Map + Sorting
"""


# json1 = '{"name":"Alex","age":"25","city":"New York"}'
# json2 = '{"name":"Alex","age":"30","city":"Los Angeles","country":"USA"}'

def findDifferentValues(json1: str, json2: str) -> list[str]:


    def parse_json(json):
        result = {}
        i = 1 # skip "{"
        while i < len(json) - 1:
            i += 1 # skip "
            start = i

            while json[i] != '"':
                i += 1

            key = json[start:i]

            i += 2 # skip " and : 

            i += 1 # skip opening "

            start = i

            while json[i] != '"':
                i += 1

            value = json[start:i]

            result[key] = value

            i += 1 # skip closing "

            if i < len(json) and json[i] == ",":
                i += 1
        return result

    json1_map = parse_json(json1)
    json2_map = parse_json(json2)

    # print(json1_map)
    # print(json2_map)
    res = []
    for key in json1_map:
        if key in json2_map and json1_map[key] != json2_map[key]:
            res.append(key)

    res.sort()
    return res

result = findDifferentValues(json1='{"name":"Alex","age":"25","city":"New York"}', json2='{"name":"Alex","age":"30","city":"Los Angeles","country":"USA"}')
print(result)

json1 = '{"a":"1","b":"2"}'
json2 = '{"a":"1","b":"2","c":"3"}'
result1 = findDifferentValues(json1, json2)
print(result1)

json1 = '{"hacker":"rank","input":"output"}'
json2 = '{"hacker":"ranked","input":"wrong"}'

result2 = findDifferentValues(json1, json2)
print(result2)