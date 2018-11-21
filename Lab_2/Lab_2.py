import xml.etree.cElementTree as ET
import string
import re
# Функция для вывода первых N строк
def print_n_lines(path, N):
    with open(path, 'r') as file:
        for x in range(N):
            print((file.readline()).strip()) # Считывает из файла одну строку и возвращает её


#myPath = 'D:/Program/Python/Lab_2/Documents/task_1.txt'
#n_lines(myPath, 6)
# task 2
path1 = "D:/Program/Python/Lab_2/Documents/a.txt"
path2 = "D:/Program/Python/Lab_2/Documents/b1.txt"
path3 = "D:/Program/Python/Lab_2/Documents/b2.txt"
a = open(path1, 'w')
b1 = open(path2, 'w')
b2 = open(path3, 'w')

with open('D:/Program/Python/Lab_2/Documents/poem.txt', 'r') as file:
    # Считывает из файла все строки в список и возвращает его
    # Текст уже находиться в файле poem.txt
    poem = file.readlines()
    for num, x in enumerate(poem):
        a.write(x)
        if num % 2:
            b1.write(x.upper())
        else:
            b2.write(x.lower())
a.close()
b1.close()
b2.close()

# task 3 izm

allWords = []
for line in poem:
    temp = line.split()
    for x in range(len(temp)):
        # Проверям чтобы последний символ не был знаком пунктуации
        allWords.append(temp[x].lower().strip(string.punctuation))

allWords.sort()
# print(allWords)

words = ET.Element("uniqueWords")
previous = allWords[0]
count = 1

uniqueWords = []

# В остортированном списк ищем слова которые повторяются и подсчитываем сколько раз
# Записываем каждое слово только один раз
for x in range(1, len(allWords)):
    current = allWords[x]
    if previous == current:
        count = count + 1
    else:
        uniqueWords.append(previous)
        ET.SubElement(words,"Word",name=previous).text = " repeated " + str(count) + " times "
        count = 1
    previous = current

tree = ET.ElementTree(words)
tree.write("c.xml")

# task 4


def get_endings(array, line):
    result = []
    for index in range(len(array)):
        ending_value = re.findall(r'\w\w\w$', array[index])
        if len(ending_value) == 1:
            result.extend([{'ending': ending_value, 'data': ({'word': array[index], 'word_position': index+1, 'line': line+1})}])
    return result

finish = []
lines = []
for i in poem:
    temp = i.split()
    lines.append(temp)

for x in range(len(lines)):
    finish.extend(get_endings(lines[x], x))

data = []
keys= []
temp = []
d = dict()
for i in range(len(finish)):
    count = 1
    find1 = finish[i].get('ending')[0]
    if find1 in d:
        d[find1].append(finish[i]['data'])
    else:
        d[find1] = [finish[i]['data']]
    for j in range(i+1, len( finish)):
        find2 = finish[j].get('ending')
        if (find1 == find2) and (find1 != None):
            data.append(finish[j].get('data'))
            finish[j].clear()
            count += 1
    if count > 1 :
        data.append(finish[i].get('data'))
for x in d:
    print(d)
print("Sorted dictionary")
for x in data:
    print(x)
for x in keys:
    print(x)
