# Kérjétek be, hogy a felhasználó mikor született!
# Írjátok ki, hogy ezek alapján hány éves!
# De ne csak egy számot, hanem a következő üzenetet:

# Mivel xxxx-ben születtél, ezért yy éves vagy.

# 1. Kérjük be, hogy mikor született! - int-é kell konvertálni
year_of_birth = int(input("Mikor születtél?"))

# 2. Számoljuk ki, hogy hány éves egy age változóba
age = 2022 - year_of_birth

# 3. Írjuk ki f-stringgel a megadott üzenetet!
print(f"Mivel {year_of_birth}-ben születtél, ezért {age} éves vagy")
