import csv
import people


def list_all(db):
    for i, data in enumerate(db):
        print(f'{i + 1}. {data}')
    return


def load():
    db = []
    with open("db.csv", "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        for i in reader:
            db.append(people.People(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
    return db


def save(db):
    with open("db.csv", "w", encoding="UTF-8") as f:
        for i in db:
            f.write(f"{i.vezetek},{i.kereszt},{i.nem},{i.szam},{i.munkahely},{i.munkahely_cim},{i.bme_tanulo}\n")
    return


def add_record():
    vezetek = input("Vezeteknév? ")
    while True:
        kereszt = input("Keresztnév? ")
        if kereszt != "":
            break
    nem = input("Neme? ")
    while True:
        szam = input("Telefon szám? ")
        if szam != "":
            break
    munkahely = input("Munkahely? ")
    munkahely_cim = input("munkahely címe? ")
    bme = input("BME-n tanul? ")

    return people.People(vezetek, kereszt, nem, szam, munkahely, munkahely_cim, bme)


def delete_record(db):
    list_all(db)

    index = int(input("Melyiket szeretne törölni? (sorszamot) "))
    db.pop(index - 1)
    return db


def modify(db):
    list_all(db)
    index = int(input("Melyiket szeretne szerkeszteni? (sorszamot) "))
    original = db[index - 1]
    choice(original)
    while True:
        valasztas = input("Szeretne mást is modositani? I/N").lower()
        if valasztas == "i":
            choice(original)
        else:
            break
    return db


def choice(original):
    print("Mit szeretne szerkeszteni?")
    print(
        "1 - Vezetéknév\n2 - Keresztnév\n3 - Nem\n4 - Telefon szám\n5 - Munkahely\n6 - Munkahely címe\n7 - BME-n tanul")
    print("===========")
    choice = int(input("Melyiket szeretne modositani? "))
    if choice == 1:
        print(f"Régi vezetéknév: {original.vezetek}")
        original.vezetek = input("Új vezetéknév? ")
    if choice == 2:
        print(f"Régi keresztnev: {original.kereszt}")
        original.keresz = input("Új keresztnév? ")
    if choice == 3:
        print(f"Régi neme: {original.nem}")
        original.nem = input("Új nem? ")
    if choice == 4:
        print(f"Régi telefonszám: {original.szam}")
        original.szam = input("Új telefonszám? ? ")
    if choice == 5:
        print(f"Régi munkahely: {original.munkahely}")
        original.munkahely = input("Új munkahely? ")
    if choice == 6:
        print(f"Régi munkahely címe: {original.munkahely_cim}")
        original.munkahely_cim = input("Új munkahely címe? ")
    if choice == 7:
        print(f"BME-s tanuló: {original.bme_tanulo}")
        original.bme_tanulo = input("BME-s tanuló? ")
    return