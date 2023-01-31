from googletrans import Translator, constants
import csv

translator = Translator()

with open('Harry.csv', 'r', encoding='utf8') as input, open('Гарри.csv', 'w', encoding='utf8') as output:
    csv_reader = csv.reader(input, delimiter=',')
    csv_writer = csv.writer(output)
    for row in csv_reader:
        if row != []:
            translation = translator.translate(row[2], dest='ru')
            csv_writer.writerow((row[0], row[1],translation.text))