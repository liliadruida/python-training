# A felhasználótól kérjetek be egy számot és írjátok ki a kétszeresét.
# Ezt egészen addig ismételjétek, amíg a felhasználó 0-át nem ír be.

number = int(input("Kérlek írj be egy számot: "))
while number > 0:
    print(number * 2)
    number = int(input("Kérlek írj be egy számot: "))
