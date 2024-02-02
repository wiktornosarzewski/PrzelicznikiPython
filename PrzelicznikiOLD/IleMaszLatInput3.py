from datetime import date

birth_year = int(input("Podaj rok urodzenia: "))
age = date.today().year - birth_year

print("Masz " + str(age) + " lat!")
