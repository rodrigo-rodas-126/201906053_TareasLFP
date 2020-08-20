import csv

print('Archivo csv')

with open('data.csv') as file:
    lector = csv.reader(file, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

    for row in lector:
        print(row)
        print(type(row))


