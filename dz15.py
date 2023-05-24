# text = "One, two, three, one, two, five. Two, five."
# words_dict = {}
# for word in text.split():
#     word = word.strip(',.').lower()
#     if word not in words_dict.keys():
#         words_dict[word] = 1
#     else:
#         words_dict[word] += 1
# print(words_dict)
#
# max_v = max(words_dict.values())
# for key, value in words_dict.items():
#     if value == max_v:
#         print(f'Слово, яке зустрічається в тексті частіше за все - "{key}"')
#         break

list = ['One', 'two', 'three', 'one', 'two', 'five', 'Two', 'five']
words = {}
for w in list:
    if w in words:
        words[w] += 1
    else:
        words[w] = 1
print(words)
