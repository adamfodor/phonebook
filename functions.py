import os
import re
import file_handle
import people


def list_all(db):
    clear()
    if len(db) == 0:
        print("Nincsen tárolt rekord")
    else:
        for i, data in enumerate(db):
            print(f'{i + 1}. {data}')

    return


def clear():
    os.system('cls')


def add_record():
    clear()
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
    clear()
    list_all(db)
    if len(db) == 0:
        return
    index = input("Melyiket szeretné törölni? (indexet irjon) ")
    if valid(index,db):
        index = int(index)
        db.pop(int(index)-1)
    else:
        error()
        return

    return db


def modify(db):
    clear()
    list_all(db)
    if len(db) == 0:
        return
    else:
        index = input("Melyiket szeretne szerkeszteni? (sorszamot) ")
        if valid(index, db):
            original = db[int(index) - 1]
            choice(original)
        else:
            error()
            return

    return db


def choice(original):
    clear()
    print("Mit szeretne szerkeszteni?")
    print(
        "1 - Vezetéknév\n2 - Keresztnév\n3 - Nem\n4 - Telefon szám\n5 - Munkahely\n"
        "6 - Munkahely címe\n7 - BME-n tanul\n0 - Vissza")
    print("===========")
    choice = input("Melyiket szeretne modositani? ")
    if valid(choice, 7):
        choice = int(choice)
    else:
        error()
        return

    if choice == 1:
        modify_vezetek(original)
    if choice == 2:
        modify_kereszt(original)
    if choice == 3:
        modify_nem(original)
    if choice == 4:
        modify_telefon_szam(original)
    if choice == 5:
        modify_munkahely(original)
    if choice == 6:
        modify_munkahely_cim(original)
    if choice == 7:
        modify_tanulo(original)
    if choice == 0:
        return
    return


def modify_vezetek(original):
    clear()
    print(f"Régi vezetéknév: {original.vezetek}")
    original.vezetek = input("Új vezetéknév? ")
    return


def modify_kereszt(original):
    clear()
    print(f"Régi keresztnev: {original.kereszt}")
    original.keresz = input("Új keresztnév? ")
    return


def modify_nem(original):
    clear()
    print(f"Régi neme: {original.nem}")
    original.nem = input("Új nem? ")
    return


def modify_telefon_szam(original):
    clear()
    print(f"Régi telefonszám: {original.szam}")
    original.szam = input("Új telefonszám? ? ")
    return


def modify_munkahely(original):
    clear()
    print(f"Régi munkahely: {original.munkahely}")
    original.munkahely = input("Új munkahely? ")
    return


def modify_munkahely_cim(original):
    clear()
    print(f"Régi munkahely címe: {original.munkahely_cim}")
    original.munkahely_cim = input("Új munkahely címe? ")
    return


def modify_tanulo(original):
    clear()
    print(f"BME-s tanuló: {original.bme_tanulo}")
    original.bme_tanulo = input("BME-s tanuló? ")
    return


def keres(db):
    clear()
    while True:
        print("Mi alapján szeretne keresni?")
        print(" 1 - Név\n 2 - Telefonszám\n 0 - Vissza")
        opcio = input("Választás:  ")
        if valid(opcio,2):
            opcio = int(opcio)
            if opcio == 1:
                keres_nev(db)
            if opcio == 2:
                keres_szam(db)
            if opcio == 0:
                break
        else:
            error()
            return
        kilep = input("Szeretne tovaább keresni? I/N? ")
        if kilep.lower() == "n":
            break
        else:
            continue
    return


def keres_nev(db):
    clear()
    nev = input("kérem a nevet: ")
    if "*" in nev:
        nev.split("*")
        pattern = nev[0] + ".*." + nev[1]
    else:
        pattern = nev
    for i in db:
        if re.search(pattern.lower(), i.nev.lower()):
            print(i)

    return


def keres_szam(db):
    clear()
    szam = input("Kérem a számot: ")
    if "*" in szam:
        szam.split("*")
        pattern = szam[0] + ".*." + szam[1]
    else:
        pattern = szam
    for i in db:
        if re.search(pattern, i.szam):
            print(i)

    return


def vcard(db):
    print("1 - Exportálni vCard-ba\n2 - Importálni vCard-ból\n0 - Vissza")
    opcio =(input("Mit szeretne csinlni? "))
    if valid(opcio,2):
        opcio = int(opcio)
        if opcio == 0:
            return
        if opcio == 1:
            file_handle.write(db)
        if opcio == 2:
            file_name = str(input("Mi a fájl neve? "))
            file_handle.read(db, file_name)
    else:
        error()
    return


def error():
    print("Hiba történt")
    print(
        "Nem számot tetszett beirni, számot irjon vagy olyan elemet probált meg választani ami nincs a tárolt adatok között")
    print("Kérem probálja újra")
    return


def valid(x, db):
    try:
        int(x)
        if isinstance(db, list):
            if 0 <= int(x) <= len(db):
                return True
        else:
            if 0 <= int(x) <= db:
                return True
    except:
        return False
