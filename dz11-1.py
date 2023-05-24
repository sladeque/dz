count = 0
summ = 0
min_a = 0
max_a = 0
even = 0
odd = 0
while True:
    a = int(input('Введіть число '))
    if a == 0:
        break
    count += 1
    summ += a
    if min_a == None or a < min_a:
        min_a = a
    if max_a == None or a > max_a:
        max_a = a
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
print(count)
print(summ)
print(min_a)
print(max_a)
print(even)
print(odd)
print(summ/count)
