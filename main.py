import functions


def main():
    db = functions.load()
    db.sort(key=lambda x: x.vezetek)
    print("Telefon könyv")
    while True:
        print("\nOpciok:\t1 - Rekordok listázása\n\t\t2 - Rekord hozzáadása\n\t\t"
              "3 - Rekord törlése\n\t\t4 - Rekord szerkesztése\n\t\t5 - Keresés\n\t\t6 - Vcard\n\t\t0 - Kilépés")
        option = (input("\nMűvelet? "))
        if option.isnumeric():
            option = int(option)
            if 6 >= int(option) >= 0:

                if option == 0:
                    functions.save(db)
                    break
                if option == 1:
                    functions.list_all(db)
                if option == 2:
                    db.append(functions.add_record())
                if option == 3:
                    functions.delete_record(db)
                if option == 4:
                    functions.modify(db)
                if option == 5:
                    functions.keres(db)
                if option == 6:
                    print("ez a funkcio meg nem mukodik")
            else:
                print("0-6-ig válasszon")
        else:
            print("Nem érvényes bemente")


if __name__ == '__main__':
    main()
