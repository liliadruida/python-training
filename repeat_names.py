# Kérjétek be a felhasználó nevét!
# Kérjétek be, hogy hányszor kerüljön kiírásra + egész szám!
# Joe 3
# Írjátok ki annyiszor a felhasználó nevét!
# JoeJoeJoe
# Aki ügyes:
# Joe Joe Joe

# Kérjétek be a felhasználó nevét!
name = input("Mi a neved?")

# Kérjétek be, hogy hányszor kerüljön kiírásra + egész szám!
count = int(input("Hányszor?"))

# Írjuk ki a nevet számszor
print(name * count)

print((name + " ") * count)