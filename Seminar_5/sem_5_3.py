# Семинар 5
# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# По умолчанию знаков препинания нет

# Вариант 1. Знаки препинания считаются частью слова, содержащего "абв"
text = 'Цуа, укп укп нрон абв абыв абв, вуву'
# ключевая строка
text_key = 'абв'
text = text.split()
text = list(filter(lambda text: text.find(text_key) == -1, text))
# из списка собираем строку с разделителем
text = ' '.join(text)
print(text)

# Вариант 2. Знаки препинания, стоящие после слова, содержащего "абв", остаются
text = 'Цуа, укп укп нрон абв абыв абв, вуву абв!'
# ключевая строка
text_key = 'абв'
text = text.split()
result = []
for i in text:
    if i.count(text_key):
        # если слово содержит не только "абв", но и знак препинания, то оставляем только знак препинания
        if i.count('.') or i.count(',') or i.count('!') or i.count('?'):
            result.append(i[-1])
    else:
        result.append(i)
# из списка собираем строку с разделителем
result = ' '.join(result)
print(result)
