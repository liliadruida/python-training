# Függvény (Function) definíció
def print_hello_world():
    print("hello")
    print("world")

# Saját függvényből lehet saját függvényt hívni
def print_hello_world_five_times():
    for i in range(0,5):
        print_hello_world()

# egy paraméteres függvény, paraméter = argument
# a paraméter nem más mint egy változó
# függvény definíció
def print_hello(text):
    print("hello")
    print(text)

# Beépített függvények: input(), print(), int(), str(), range()
fruits = ["meggy", "cseresznye", "körte"]

# len()
print(len(fruits))  # length - hossz

print(len("hello world"))  # string hosszát adja vissza

# függvények: névvel ellátott utasítás csoport

# DRY nem teljesül
#print("hello")
#print("world")

#print("hello")
#print("world")

print_hello_world() # meghívom a függvényt, végrehajtásra kerülnek a függvényben lévő utasítások

print_hello_world()

print("-------")

print_hello_world_five_times()


print_hello("joe")
print_hello("jack")

text = input("Please introduce yourself: ")
print_hello(text)
