def find_longest_word(sentence):
    words = sentence.split()  # Розділення рядка на слова за пробілами
    longest_word = max(words, key=len)  # Знаходження найдовшого слова за довжиною
    return longest_word

input_string = "привіт сеген ти уже виздоровів ?"
print("Найдовше слово у рядку:", find_longest_word(input_string))
