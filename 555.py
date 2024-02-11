def capitalize_first_letter(sentence):
    words = sentence.split()  # Розділення рядка на слова за пробілами
    capitalized_words = [word.capitalize() for word in words]  # Заміна перших літер на великі
    return ' '.join(capitalized_words)  # Об'єднання слів у рядок з великими першими літерами

input_string = "привіт сеген як ти там"
print(capitalize_first_letter(input_string))
