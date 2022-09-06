# Írjuk ki 5x egymás után a nevünket ciklussal
#print("István\n" * 5)

#for i in range(5):  # ciklus fej#
#    print(i)
#    print("István")  # ciklus törzs

# for >>> kulcsszó
# i >>> ciklusváltozó
# in >>> kulcsszó
# range(5) >>> függvény

# Feladat: Írj egy ciklust, ami kíírja a számokat 1-től 100-ig egymás alá!
for i in range(100):
    print(i + 1)

# Feladat: Írd ki egymás után a neved 5x, írd elé a sorszámot is!
for i in range(5):
    print(f" {i + 1}. Emese")

# Feladat: Írj egy ciklust, amely 1-től 10-ig kiíírja a számokat és azok
# négyzetét is egy új sorba!
for i in range(10):
    j = i + 1
    result = j ** 2
    print(f"A {j} szám négyzete: {result}")

# i felveszi a következő értékeket: 5 <= i < 10
for i in range(5, 10):
    print(i)

# harmadik paraméter a lépés
for i in range(10, 20, 2):
    print(i)

# lépés negatív szám, csökkenti, esetünkben 10-től 1-ig
for i in range(10, 0, -1):
    print(i)


