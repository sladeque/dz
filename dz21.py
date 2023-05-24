def vowel_words(words):
    b = "aeiou"
    c = []
    non_vowel_words = 0
    for word in words:
        if word[0].lower() in b:
            c.append(word)
        else:
            non_vowel_words += 1
    return (c, non_vowel_words)

print(vowel_words(['apricot', 'apple', 'Dog', 'cucumber', 'Zebra', 'Bat', 'Orange', 'Lemon']))