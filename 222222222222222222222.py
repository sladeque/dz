a = 0
b = 1
n = int(input (" Введіть кількість чисел в послідовності: "))
print(n,"=>",a , end=',')
for c in range(0, n):
    a, b = b, a + b
    print(a, end= ',')



