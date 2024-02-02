from datetime import date
once = False
while True:
    if once: 
        user_input = input("Wpisz r, aby wykonać ponownie: ")
    else:
        user_input = "r"
    if user_input == "r":
        while True:
            birth_year = input("Podaj rok urodzenia: ")
            if birth_year.isnumeric():
                age = date.today().year - int(birth_year)
                print("Masz " + str(age) + " lat!")
                once = True
                break
            else:
                print("Niepoprawny format roku urodzenia. Spróbuj ponownie.")
            continue
    else:
        break
