# Logikai kifejezések

# Logikai literál
True
False
print(type(True))

# Ha van tojás, és van szalonna, akkor csináljunk ham&eggs-t
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Vagy
# Ha éhes vagy vagy 16:00 múlt, akkor egyél
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negáció
print(not True)
print(not False)

# Kombinálva
print(((not True) or (False)) and (not False))

# Összehasonlítások: relációs jelek
print(1 < 2)
print(1 > 2)
print(1 == 2)  # Vigyázz, összehasonlítás KÉT egyenlőség jel
print(1 >= 2)
print(1 >= 1)

print(1 < 5 < 10)

# Hogyan döntjük el egy számról, hogy páros-e?
# A számoz osztjuk kettővel, és ha páros a maradéka 0
print(9 % 2 == 0)
print(10 % 2 == 0)
print(11 % 2 == 0)
print(12 % 2 == 0)

# Kérjünk be a felhasználótól egy számot, és írjuk ki, hogy False, ha
# a szám páros, írjuk ki, hogy True, ha a szám páratlan

number = int(input("Kérem adjon meg egy számot: "))
result = (number % 2 == 0)
print(result == False)

