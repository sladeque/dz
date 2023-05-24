lst2 = ['red', 1, 'green', 'white']
lst1 = ['red', 'white', 1]
lst3=list(set(lst1) & set(lst2))

print(lst3)