#1
def reverse_string(n):
    if len(n) == 0:
        return n
    else:
        return reverse_string(n[1:]) + n[0]
n = reverse_string(input('Введіть слово 1: ')[:100])

print('перевернуте слово 1:', (n))

#2
def rev(a):
    b='перевернуте слово 2: '
    for i in range(len(a)-1,-1,-1):
        b+=a[i]
    return b

n = rev(input('Введіть слово 2: ')[:100])
print(n)

