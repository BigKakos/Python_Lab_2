from csv import reader
import xml.etree.ElementTree as ET

def open_table():
    try:
        with open('books-en.csv', 'r') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            table = table[1:]
            return table
    except FileNotFoundError:
        print('Файл не найден!')
        return 0

def count_name(n=30):
    count = 0
    for i in open_table():
        if len(i[1]) > n:
            count += 1
    print(count)

def search():
    author = input('Введите автора: ')
    names = []
    for i in open_table():
        if i[2] == author and float(i[6].replace(',', '.')) < 200:
            names.append(i[1])
    if len(names) == 0:
        print('книги не найдены')
    else:
        print(names)

def generator():
    for line in open_table()[:20]:
        author = line[2]
        title = line[1]
        year = line[3]
        yield f'{author}. {title} - {year}'

def new_file():
    file = open('new_file.txt', 'w')
    for n, i in enumerate(generator(), 1):
        file.write(f'{n}. {i}\n')

def parsxml():
    tree = ET.parse('currency.xml')
    root = tree.getroot()
    res = {}
    for valute in root.findall('Valute'):
        num_code = int(valute.findtext('NumCode'))
        char_code = valute.findtext('CharCode')
        res[num_code] = char_code
    print(res)

def publishers():
    res = set()
    for i in open_table():
        res.add(i[4])
    print(res)

def famous_books():
    table = open_table()
    sorted_table = sorted(table, key=lambda x: int(x[5]), reverse=True)
    res = []
    for i in range(20):
        res.append(sorted_table[i][1])
    print(res)

# count_name()
# search()
# new_file()
# parsxml()
# publishers()
# famous_books()