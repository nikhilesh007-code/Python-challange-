import math
import copy

def create():
    return [
        {"id": 1, "marks": 78, "attendance": 80, "scores": [15, 20]},
        {"id": 2, "marks": 65, "attendance": 75, "scores": [12, 18]}
    ]

def change(arr, r):
    k = r % 3
    if k == 0:
        k = 1
    for i in range(len(arr)):
        if i % k == 0:
            val = arr[i]["marks"]
            arr[i]["marks"] = int(val + math.sqrt(val))
            arr[i]["attendance"] -= 5
            arr[i]["scores"][0] += 2
    return arr

def stats(a, b):
    x = [i["marks"] for i in a]
    y = [i["marks"] for i in b]
    m = sum(y) / len(y)
    d = abs((sum(x) / len(x)) - m)
    return m, d

roll = 24110011589

data = create()

s1 = data.copy()
s2 = copy.deepcopy(data)

change(s1, roll)
change(s2, roll)

mean, drift = stats(data, s2)

print(data)
print(s1)
print(s2)
print(drift)
print(mean)
