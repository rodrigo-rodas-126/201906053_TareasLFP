import json

print('Archivo json')

def readJ():
    file = open('data.json')
    registros = json.load(file)
    for registro in registros:
        print(registro)
        print(type(registro))

readJ()

