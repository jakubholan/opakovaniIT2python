import random

# 1. Vytvořte proměnnou, do které vložíte své jméno.
jmeno = "Jakub"

# 2. Vytvořte proměnnou, do které vložíte své příjmení.
prijmeni = "Holan"

# 3. Vypište tyto dvě proměnné do konzole.
print(jmeno + " " + prijmeni)

# 4. Vytvořte vstup pro uživatele, který bude moct zadat pouze věk.
vek = int(input("Jaký je váš věk (pouze číslo): "))

# 5. Vypište v konzoli délku první proměnné a druhé proměnné.
print(len(jmeno) + len(prijmeni))

# 6. Vytvořte proměnnou, do které uložíte hodnotu 6.
a = 6

# 7. Vytvořte cyklus, který bude mít 5 opakování a při každém opakování se přičte hodnota 3.
for x in range(5):
    a += 3

# 8. Vypište v konzoli výslednou hodnotu po 5 cyklech.
print("Výsledek proměnné je:", a)

# 9. Podmínka pro uživatele k zadání věku.

vek = int(input("Zadejte svůj věk: "))

# 10. Vytvořte proměnnou, do které uloží program náhodnou hodnotu od 1-10 a vypište ji do konzole.
print(random.randint(1, 10))