import csv
import people
import functions


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


def read(db, file):
    data = []
    try:
        f = open(file, "r", encoding="UTF-8")
        for row in f:
            row = row.split(":")[1].strip("\n")
            data.append(row)
        nev = data[2].split(";")
        vezetek = nev[0]
        kereszt = nev[1]

        nem = data[4]
        szam = data[5]
        munkahely = data[6]
        return db.append(people.People(vezetek, kereszt, nem, szam, munkahely, "", ""))
    except:
        print("rossz fájlnév vagy kiterjesztés")
        return


def write(db):
    functions.list_all(db)
    rekord = db[int(input("Melyik rekordot szeretné exportálni? ")) - 1]
    with open("output.vcf", "wt", encoding="utf-8") as f:
        f.write("BEGIN:VCARD\n")
        f.write("VERSION:3.0\n")
        f.write(f"N:{rekord.vezetek};{rekord.kereszt}\n")
        f.write(f"FN:{rekord.vezetek} {rekord.kereszt}\n")
        f.write(f"GENDER:{rekord.nem}\n")
        f.write(f"TEL:{rekord.szam}\n")
        f.write(f"ORG:{rekord.munkahely}\n")
        f.write("END:VCARD")
    return
