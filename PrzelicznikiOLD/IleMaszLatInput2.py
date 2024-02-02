from datetime import date

birth_date = input("Podaj datę urodzenia w formacie RRRR-MM-DD: ")
year, month, day = map(int, birth_date.split("-"))
age = date.today().year - year - ((date.today().month, date.today().day) < (month, day))

print("Masz " + str(age) + " lat!")
