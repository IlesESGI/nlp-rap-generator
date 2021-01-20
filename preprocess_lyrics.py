import json

with open('lyrics.json') as json_file:
    data = json.load(json_file)

with open("example.json","w") as jsonfile:
    for elemnt in data['PNL']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Ninho']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Jul']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Damso']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Kaaris']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['RK']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['PLK']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Sadek']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Sofiane']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Vald']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Lefa']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Nekfeu']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Booba']['songs']:
        print(elemnt['lyrics'],jsonfile)
    for elemnt in data['Rohff']['songs']:
        print(elemnt['lyrics'],jsonfile)