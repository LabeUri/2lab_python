def count_words(sentence):
    words = sentence.split()
    return len(words)

input_string = "сеген ти хворий чи уже виздоровів"
print("Кількість слів у рядку:", count_words(input_string))
