"""
2. Concurrent Session Limit Breaches
Problem

A system records n user-session events in chronological order.
For each event, you are given:
timestamps[i]
userIds[i]
actions[i]
where:

timestamps[i] is the event time.
userIds[i] identifies the user.
actions[i] is either "login" or "logout".

Each user has an active session count, initially 0.

Process events in the given order.

For each event:
"login" increases the user's active-session count by 1.
"logout" decreases the user's active-session count by 1 only if the current count is greater than 0.
A user breaches the session limit if their active-session count becomes strictly greater than m at any point.
Return all unique user IDs that breach the limit.
The result must be sorted in lexicographical order.
Example 1
Input:
timestamps = [1, 2, 3, 4]
userIds = ["A", "A", "A", "A"]
actions = ["login", "login", "login", "logout"]
m = 2

Output:
["A"]
Explanation
The session count for A changes as follows:
time 1: login   -> 1
time 2: login   -> 2
time 3: login   -> 3   <-- breach
time 4: logout  -> 2
Because 3 > 2, user "A" breached the limit.

Example 2
Input:
timestamps = [1, 2, 3, 4, 5, 6]
userIds = ["A", "B", "A", "B", "A", "B"]
actions = ["login", "login", "login", "login", "logout", "login"]
m = 2

Output:
["B"]
Explanation
For user A:
login -> 1
login -> 2
logout -> 1
A never exceeds 2.
For user B:
login -> 1
login -> 2
login -> 3
B exceeds the limit, so:
["B"]

Example 3
Input:
timestamps = [1, 2, 3]
userIds = ["A", "A", "A"]
actions = ["logout", "login", "logout"]
m = 1

Output:
[]
Explanation
The first logout does nothing because the current count is already 0.
logout -> 0
login  -> 1
logout -> 0
The count never becomes greater than 1.

Constraints
1 <= n <= 100000

timestamps.length == userIds.length == actions.length

timestamps are in non-decreasing order.

actions[i] is either "login" or "logout".

1 <= m <= 100000
Function
def getLimitBreaches(    timestamps: list[int],    userIds: list[str],    actions: list[str],    m: int) -> list[str]:
Pattern
Hash Map + Set + Simulation + Sorting
The recognition rule for this one is:
Events happening over time + maintain per-user state → simulation with a dictionary.
And:
Need each violating user only once → set.
"""
def getLimitBreaches(    timestamps: list[int],    userIds: list[str],    actions: list[str],    m: int) -> list[str]:
    map1 = {}
    breached = set()
    for i in range(len(timestamps)):
        if actions[i] == "login":
            map1[userIds[i]] = map1.get(userIds[i], 0) + 1
            if map1[userIds[i]] > m:
                breached.add(userIds[i])

        elif actions[i] == "logout":
            if userIds[i] in map1 and map1[userIds[i]] > 0:
                map1[userIds[i]] -= 1
    return sorted(breached)

line = "________________________________"
# 1. Basic breach
timestamps = [1, 2, 3]
userIds = ["A", "A", "A"]
actions = ["login", "login", "login"]
m = 2
# Expected: ["A"]
print(getLimitBreaches(timestamps, userIds, actions, m))


print(line)

# 2. No breach
timestamps = [1, 2, 3, 4]
userIds = ["A", "A", "A", "A"]
actions = ["login", "login", "logout", "login"]
m = 2
# Counts: 1 -> 2 -> 1 -> 2
# Expected: []
print(getLimitBreaches(timestamps, userIds, actions, m))

print(line)

# 3. Logout when count is already 0
timestamps = [1, 2, 3]
userIds = ["A", "A", "A"]
actions = ["logout", "login", "logout"]
m = 1
# Expected: []
print(getLimitBreaches(timestamps, userIds, actions, m))

print(line)

# 4. Multiple users, one breaches
timestamps = [1, 2, 3, 4, 5, 6]
userIds = ["A", "B", "A", "B", "A", "B"]
actions = ["login", "login", "login", "login", "logout", "login"]
m = 2
# Expected: ["B"]
print(getLimitBreaches(timestamps, userIds, actions, m))

print(line)

# 5. Multiple users breach
timestamps = [1, 2, 3, 4, 5, 6, 7, 8]
userIds = ["B", "A", "B", "A", "B", "A", "C", "C"]
actions = ["login", "login", "login", "login", "login", "login", "login", "logout"]
m = 2
# A reaches 3
# B reaches 3
# Expected: ["A", "B"]
print(getLimitBreaches(timestamps, userIds, actions, m))

print(line)


# 6. Same user breaches more than once
timestamps = [1, 2, 3, 4, 5, 6]
userIds = ["A", "A", "A", "A", "A", "A"]
actions = ["login", "login", "login", "logout", "login", "login"]
m = 2
# A breaches at 3, later again
# Should still appear only once
# Expected: ["A"]
print(getLimitBreaches(timestamps, userIds, actions, m))

print(line)


# 7. Limit of 1
timestamps = [1, 2, 3, 4]
userIds = ["A", "B", "A", "B"]
actions = ["login", "login", "login", "logout"]
m = 1
# A: 1 -> 2 => breach
# B: 1 -> 0
# Expected: ["A"]

print(getLimitBreaches(timestamps, userIds, actions, m))

print(line)


# 8. Lexicographical sorting
timestamps = [1, 2, 3, 4, 5, 6]
userIds = ["B2", "A9", "B2", "A9", "B2", "A9"]
actions = ["login", "login", "login", "login", "login", "login"]
m = 2
# Expected: ["A9", "B2"]
print(getLimitBreaches(timestamps, userIds, actions, m))

print(line)


# 9. User breaches, then logs out below the limit
timestamps = [1, 2, 3, 4, 5]
userIds = ["A", "A", "A", "A", "A"]
actions = ["login", "login", "login", "logout", "logout"]
m = 2
# Once breached, still included even though count later falls
# Expected: ["A"]

print(getLimitBreaches(timestamps, userIds, actions, m))

print(line)