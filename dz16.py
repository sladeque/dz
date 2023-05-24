lst1 = [1, 8, 12, world]
lst2 = [1, 7, 12, world]
lst3 = []

for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
        lst3.append(lst1[i])

print(lst3)