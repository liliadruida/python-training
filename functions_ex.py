# Írjátok meg a signum függvényt!
# Ha a szám kisebb, mint 0, akkor -1-et ad vissza
# Ha 0, akkor 0-át ad vissza
# Ha nagyobb mint 0, akkor 1-et ad vissza
def signum(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1

def signum_struct(n):
    if n < 0:
        result = -1
    elif n == 0:
        result = 0
    else:
        result = 1
    return result


# Írjatok egy függvényt ami vár egy egész számot és visszaadja
# annak abszolút értékét!
def absolute(n):
    if n >= 0:
        return n
    else:
        return -n


# Struktúrált programozás: minden függvényben CSAK egy
# return utasítás lehet. Ez csak stílus beli különbség
def abs_structured(n):
    if n < 0:
        result = -n
    else:
        result = n
    return result


# Írjatok egy függvényt, mely várja a téglalap a és b oldalát, és
# visszaadja a területet!
def area(a, b):
    return a * b


# Írjatok egy függvényt, mely várja a téglalap a és b oldalát, és
# visszaadja a kerületet!
def calculate_perimeter(a, b):
    return 2 * (a + b)


# Írjatok egy függvényt ami vár két számot és visszaadja a
# kettő közül a nagyobbat!
def max(a, b):
    if a > b:
        return a
    else:
        return b


# Vár egy számot és visszaadja a "páros" szöveget, ha páros,
# ellenkező esetben hogy "páratlan"
def num_type(a):
    if a % 2 == 0:
        return "páros"
    else:
        return "páratlan"

def num_type_struct(a):
    if a % 2 == 0:
        type = "páros"
    else:
        type = "páratlan"
    return type


# Ha a függvény boolean értéket ad vissza, akkor
# logikai függvény: True vagy False
# Azért szeretjük őket, mert nagyon jól lehet őket használni feltételekben

# Írj egy is_even nevű függvényt, mely a paraméteréről
# eldönti, páros-e!
# True-t adjon vissza, ha páros, False értéket adjon vissza
# ha páratlan

def is_even(n):
    return n % 2 == 0


print(signum(16))

print("-----")

print (absolute(3))

print("-----")

print(area(3, 7))

print("-----")

print(calculate_perimeter(3, 7))

print("-----")

print(max(5, 10))

print("-----")

print(num_type(1622))

print("-----")

print(is_even(1))
print(is_even(2))

print("-----")

if is_even(5):
    print("Ez egy szép páros szám")
else:
    print("Ez egy páratlan szám")