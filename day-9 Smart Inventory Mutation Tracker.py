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

# Personalized Roll Number
roll = 24110011589

main_data = get_data()

# Copies
copy1 = main_data.copy()          # Shallow Copy
copy2 = copy.deepcopy(main_data) # Deep Copy

# Update
update_items(copy1, roll)
update_items(copy2, roll)

# Print Results
print("Original:", main_data)
print("Shallow Copy:", copy1)
print("Deep Copy:", copy2)

# Comparison
c1, u1 = check_diff(main_data, copy1)
c2, u2 = check_diff(main_data, copy2)

print("Shallow Changed:", c1, "Unchanged:", u1)
print("Deep Changed:", c2, "Unchanged:", u2)

print("Shallow Count:", (len(c1), len(u1)))
print("Deep Count:", (len(c2), len(u2)))
