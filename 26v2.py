with open('lorem.txt', 'r', encoding = 'utf-8') as f:
    text = f.read().split()

d = {}
for word in text:
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1

with open('stats.txt', 'w', encoding = 'utf-8') as f:
    for key, value in d.items():
        f.write(f'{key}: {value}\n')