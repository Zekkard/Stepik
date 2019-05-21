# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое последнего файла из набора, как ответ на это задание.
import requests
with open('dataset_3378_3.txt') as txt:
    a = txt.readline().strip()
print(a)
a = str(requests.get(a).text)
b = 'https://stepic.org/media/attachments/course67/3.6.3/'
while 'we' not in a:
    print(a)
??? a = requests.get(b + a).text
print(a)