# Kérj be egy egész számot, és írd ki addig az összes egész páros számot!
# Pl. 8, akkor legyen kiírva: 2, 4, 6, 8
# Pl. 3, akkor legyen kiírva: 2
# Pl. 12, akkor legyen kiírva: 2, 4, 6, 8, 10, 12

number = int(input("Kérlek írj be egy egész számot: "))
for i in range(2, number + 1, 2):
    print(i)

    