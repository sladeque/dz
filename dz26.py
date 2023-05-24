with open('lorem.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text = text.lower()
    text_words = text.split()
    words_dict = {}
    for word in text_words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

with open('stats.txt', 'w', encoding='utf-8') as file:
    for word, count in words_dict.items():
        file.write(f'{word}: {count}\n')
