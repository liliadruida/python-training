# A felhasználótól kérjetek be egy számot és írjátok ki a kétszeresét.
# Ezt egészen addig ismételjétek, amíg a felhasználó 0-át nem ír be.

# DRY - don't repeat yourself

#number = int(input("Kérlek írj be egy számot: "))
number = 100
while number > 0:
    number = int(input("Kérlek írj be egy számot: "))
    print(number * 2)
    
