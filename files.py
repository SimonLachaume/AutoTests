text = input('Введите текст: ')

file = open("files/test_text.txt", "w")
file.write(text)
file.close()
file_read = open("files/test_text.txt", "r")
explore_text = file_read.read()
print("Пользователь записал в файл: " + str(explore_text))
file_read.close()



