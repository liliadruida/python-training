# String egy adatszerkezet, hiszen karakterekből áll
name = "John Doe"
for c in name:  # végigmegy a karaktereken
    print(c)

print("-----")

# Összeszámolja a névben lévő o betűket
count = 0
for c in name:
    if c == "o":
        count += 1
print(count)

print("-----")

# Így lehet hozzáférni bármelyik karakterhez a str-ben
print(name[3])

print("-----")

# Szeletelés / slicing
# str szeletkéket tudunk kivágni
print(name[1:4])

print("-----")

print(len(name))

print("-----")

print("John" in "John Doe")

print("-----")

if "John" in name:
    print("Na ez is egy újabb John")

print("-----")

# Stringeknek vannak saját függvényeik: metódusok

print(name.upper())  # a függvényt a name változón hívjuk meg

print("-----")

fruit = "                       alma                          "
print(fruit.strip())

print("-----")

print("john" in "Jack Jane John")
print("joHn".upper() in "Jack Jane John".upper())

print("-----")


