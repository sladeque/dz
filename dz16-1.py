lst2 = [1, 1, 5, 'white']
lst1 = [1, 'white', 5]
lst3=list(set(lst1) & set(lst2))

print(len(lst3))