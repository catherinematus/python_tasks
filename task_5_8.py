text = input('Введите фразу \n')
new_text = text.split(' ')
for i in range(int(len(new_text) / 2)):
    c = new_text[i]
    new_text[i] = new_text[len(new_text) - 1 - i]
    new_text[len(new_text) - 1 - i] = c
print((' ').join(new_text))
