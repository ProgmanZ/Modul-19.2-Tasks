# Задача 3. Гистограмма частоты

user_text = input('Введите текст: ').lower()
text_dict = dict()

for symbol in sorted(user_text):
    if symbol in text_dict:
        text_dict[symbol] += 1
    else:
        text_dict[symbol] = 1

for key in text_dict.keys():
    print('{0}:{1}'.format(key, text_dict[key]))

print('Максимальная частота:', max(text_dict.values()))

