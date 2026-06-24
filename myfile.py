a = [1,2,3,3,4,5,7,8,10,6,6]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            print(f"Duplicate found: {a[i]} at indices {i} and {j}")