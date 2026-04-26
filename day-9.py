import copy

def get_data():
    return [
        {"item": "Laptop", "details": {"price": 50000, "stock": 10, "supplier": {"rating": 4.5}}},
        {"item": "Phone", "details": {"price": 20000, "stock": 25, "supplier": {"rating": 4.2}}}
    ]

def update_items(arr, r):
    pos = r % len(arr)
    for i in range(len(arr)):
        if i == pos:
            arr[i]["details"]["price"] = int(arr[i]["details"]["price"] * 0.9)
            arr[i]["details"]["stock"] += 5
    return arr

def check_diff(a, b):
    changed = []
    unchanged = []
    for i in range(len(a)):
        if a[i] == b[i]:
            unchanged.append(a[i]["item"])
        else:
            changed.append(a[i]["item"])
    return changed, unchanged

roll = 24110011589

main_data = get_data()

copy1 = main_data.copy()
copy2 = copy.deepcopy(main_data)

update_items(copy1, roll)
update_items(copy2, roll)

print(main_data)
print(copy1)
print(copy2)

c1, u1 = check_diff(main_data, copy1)
c2, u2 = check_diff(main_data, copy2)

print(c1, u1)
print(c2, u2)

print((len(c1), len(u1)))
print((len(c2), len(u2)))