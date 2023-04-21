import codecs
fileObj = codecs.open("leasing.txt", "r", "utf_8_sig")
text = fileObj.read()  # или читайте по строке
l = text.split(" ")

unions = ['и', 'ни-ни', 'тоже', 'также', 'а', 'но', 'однако', 'зато', 'же', 'или', 'либо',
        'то-то', 'что', 'чтобы', 'будто','когда', 'пока', 'едва', 'если','раз', 'ибо', 'чтобы',
        'дабы', 'хотя', 'хоть', 'пускай', 'как', 'словно','кто', 'что', 'каков', 'который', 'куда',
        'откуда', 'где', 'сколько', 'почему', 'зачем', 'как']
for union in unions:
    while union in l:
        l.remove(union)

new_text = " ".join(l)

my_file = open("newleasing.txt", "w")
my_file.write(new_text)
my_file.close()
