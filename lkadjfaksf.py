class CupOfCoffee:
    def __init__(self, coffee_type, drinking_type, price):
        self.coffee_type = coffee_type
        self.drinking_type = drinking_type
        self.add_on = []
        self.price = price

    def set_add_on(self, one_add_on, one_add_on_price):
        if one_add_on in self.add_on:
            print("ERROR: Invalid input!")
            return
        self.add_on.append(one_add_on)
        self.price += one_add_on_price

    def set_coffee_type(self, name):
        self.coffee_type = name

    def set_drinking_type(self, name):
        self.drinking_type = name

    def __repr__(self):
        if len(self.add_on) == 0:
            return f" This cup is {lowerF(typeReturn(self.drinking_type.lower()))} {self.coffee_type} with no add on, {self.price} baht."
        elif len(self.add_on) == 1:
            return f" This cup is {lowerF(typeReturn(self.drinking_type.lower()))} {self.coffee_type} with {self.add_on[0]}, {self.price} baht."
        else:
            return f' This cup is {lowerF(typeReturn(self.drinking_type.lower()))} {self.coffee_type} with {", ".join(self.add_on[:-1])} and {self.add_on[-1]}, {self.price} baht.'


class CustomerBill:
    def __init__(self, name):
        self.name = name
        self.ordered_coffee = []

    def add_ordered_coffee(self, aCupOfCoffeeObject):
        self.ordered_coffee.append(aCupOfCoffeeObject)

    def receipt(self):
        txt = f"++++++++++++++++++++++++++++++++\n"
        txt += f"      CPE38 **StarBUG Cafe      \n"
        name = f"Kun {self.name}'s Receipt"
        txt += f"{name:^32}\n"
        txt += f"++++++++++++++++++++++++++++++++\n"
        txt += f'{"Description":<27}{"Price":5}\n'
        all_price = 0
        for cup in self.ordered_coffee:
            all_price += int(cup.price)
            cup_type = f"{typeReturn(cup.drinking_type)} {cup.coffee_type}"
            txt += f"{cup_type:<27}{cup.price:>5}\n"
            for add_on in cup.add_on:
                txt += f" + {add_on}\n"
            txt += f"\n"
        all_price = f'{all_price:,}'
        txt += f'{"Total":<27}{all_price:>5}\n'
        txt += f"++++++++++++++++++++++++++++++++\n"
        txt += f" Thank you, please come back :) \n"
        txt += f"++++++++++++++++++++++++++++++++\n"
        return txt



def readMenu(fn="CoffeeMenu01.txt"):  # นำฟังชันนี้ไปใช้อ่านเมนูกาแฟ โดยไม่ต้องส่งซ้ำ
    with open(fn) as fd:
        return fd.read()

def readAddon(fn="CoffeeMenuAddOn01.txt"):  # นำฟังชันนี้ไปใช้อ่านเมนูกาแฟ โดยไม่ต้องส่งซ้ำ
    with open(fn) as fd:
        return fd.read()

coffee_menu_filename = input('Enter Coffee Menu available today (filename): ')
coffee_menu_CSV = readMenu(coffee_menu_filename)
addon_menu_filename = input('Enter AddOn Menu available today (filename): ')
add_on_menu_CSV = readMenu(addon_menu_filename)

read = coffee_menu_CSV
readad = add_on_menu_CSV
customers = []

def Menu(readMenu):
    read = readMenu
    line = read.splitlines()
    line = [i for i in line if i != ""]
    print("Welcome to CPE38 **StarBUG Cafe!")
    print("+++++++++++++ MENU +++++++++++++")
    c = f'{"Coffee":<15}'
    h = f'{"Hot":<5}'
    co = f'{"Cold":<6}'
    f = f'{"Frappe"}'
    print(f"{c}{h}{co}{f}")
    count = 1
    for i in line:
        l = i.split(",")
        l = [i.strip(" ") for i in l]
        if len(l) != 1:
            l1 = f"{l[0]:<13}"
            l2 = f"{l[1]:>3}"
            l3 = f"{l[2]:>5}"
            l4 = f"{l[3]:>5}"
            print(f"{count}.{l1}{l2} {l3} {l4}")
        else:
            break
        count += 1

def lowerF(name) :
    if name == 'Hot' :
        return 'hot'
    elif name == 'Cold' :
        return 'cold'
    elif name == 'Frappe' :
        return 'frappe'


def Name(read) : 
    l = []
    for i in read :
        l.append(i[0])
    return l 

def readAddon(readAddon):
    read = readAddon
    line = read.splitlines()
    line = [i for i in line if i != ""]
    print("++++++++++++ ADD-ON ++++++++++++")
    count = 1
    for i in line:
        x = i.split(",")
        x1 = x[0]
        x2 = x[1]
        print(f"{count}.{x1:<16} {x2:>5}")
        count += 1
    print("++++++++++++++++++++++++++++++++")
    print()

def addOnList(readad):
    l = []
    line = readad.splitlines()
    line = [i for i in line if i != ""]
    for i in line:
        x = i.split(",")
        l.append(x[0])
    l.insert(0, 0)
    return l


def CoffeePrice(read):
    line = read.splitlines()
    line = [i for i in line if i != ""]
    list_coffee = []
    for i in line:
        l = i.split(",")
        l = [i.strip(" ") for i in l]
        list_coffee.append(l)
    return list_coffee


def coffeePriceTypeofCoffee(read):
    coffee_dicts = [
        {"Name": item[0], "h": int(item[1]), "c": int(item[2]), "f": int(item[3])}
        for item in read
    ]
    return coffee_dicts


def NumMenu(read):
    l = []
    for i in read:
        l.append(i[0])
    l.insert(0, 0)
    return l



def checktype(name):
    if name == "Americano":
        return ["H", "C"]
    elif name == "Cappuccino":
        return ["H", "C", "F"]
    elif name == "Latte":
        return ["H", "C", "F"]
    elif name == "Mocha":
        return ["H", "C", "F"]
    elif name == "Espresso":
        return ["H"]
    elif name == "Macchiato":
        return ["H", "C", "F"]

def priceOfaddon(readad):
    l = []
    line = readad.splitlines()
    line = [i for i in line if i != ""]
    for i in line:
        x = i.split(",")
        l.append(x[1])
    l.insert(0, 0)
    l = [int(i) for i in l]
    return l


def checkIndentHowMuch(checkx):
    if checkx == "h":
        return 1
    elif checkx == "c":
        return 2
    elif checkx == "f":
        return 3



def typeReturn(type):
    if type == "h":
        return "Hot"
    elif type == "c":
        return "Cold"
    elif type == "f":
        return "Frappe"
    
def get_customer(name):
    for c in customers:
        if c.name == name:
            return c
    return None

def summary():
    print(f"++++++++++++++++++++++++++++++++")
    print(f"      CPE38 **StarBUG Cafe      ")
    print(f"  Report for Coffee sold today  ")
    print(f"++++++++++++++++++++++++++++++++")
    d = {}
    total_price = 0
    for c in customers:
        total_price += sum([int(order.price) for order in c.ordered_coffee])
        for cup in c.ordered_coffee:
            try:
                d[cup.coffee_type] += 1
            except:
                d[cup.coffee_type] = 1
    for key in Name(CoffeePrice(read)):
        try:
            if d[key] < 2:
                print(f" {key:<24}{str(d[key])} cup")
            else:
                print(f" {key:<24}{str(d[key])} cups")
        except:
            pass

    print()
    x = f'{total_price:,}'
    print(f"Total sold amount {x:>9} baht")
    print(f"++++++++++++++++++++++++++++++++")
    print(f"       What's a good day!       ")
    print(f"++++++++++++++++++++++++++++++++")
    print()

list_addon = addOnList(readad)
coffee_price = CoffeePrice(read)
snow = "hcf"

numeofMenu = NumMenu(CoffeePrice(read))

dict_for_result = {}
list_for_money = []

def select_coffee_type(i = 0):
    try:
        typec = int(input(f"Cup #{i+1}, please select type of coffee: "))
        if typec <= 0:
            return select_coffee_type(i)
        x = NumMenu(CoffeePrice(read))[typec]
        return x, typec
    except:
        print(" ERROR: Invalid input!")
        return select_coffee_type(i)

def select_drinking_type(types, i = 0):
    try:
        if len(types) == 1:
            return types[0].lower()
        drinkingtype = (
            input(f'Cup #{i+1}, please select drinking type ({",".join(types)}): ')
        ).lower()
        if drinkingtype.upper() not in types:
            print(" ERROR: Invalid input!")
            return select_drinking_type(types, i)
        return drinkingtype
    except:
        print(" ERROR: Invalid input!")
        return select_drinking_type(types, i)

def get_cup():
    try:
        many_cup = int(input("How many cups of coffee to order? "))
        if many_cup <= 0:
            print(" ERROR: Invalid input!")
            return get_cup()
        return many_cup
    except:
        print(" ERROR: Invalid input!")
        return get_cup()


def runStarBUGcafe_main():
    while True:
        Menu(read)
        readAddon(readad)
        name = input("Enter customer's name: ")
        if name == "Good Day":
            summary()
            break
        customer = get_customer(name)
        if customer is None:
            classofname = CustomerBill(name)
        else:
            classofname = customer
        # many_cup = int(input("How many cups of coffee to order? "))
        # while many_cup <= 0:
        #     print("ERROR: Invalid input!")
        #     many_cup = int(input("How many cups of coffee to order? "))
        many_cup = get_cup()
        for i in range(many_cup):
            l = []
            x, typec = select_coffee_type(i)
            checkx = checktype(x)
            drinkingtype = select_drinking_type(checkx,i)
            Cupbycup = CupOfCoffee(
                x, drinkingtype, int(coffee_price[typec - 1][checkIndentHowMuch(drinkingtype)])
            )
            if coffee_price == 0:
                print(" ERROR: Invalid input!")
                continue
            while True:
                selec_addon = input(f"Cup #{i+1}, please select add on (enter for exit): ")
                if selec_addon == "" :
                    break
                try:
                    index_selec = int(selec_addon)
                    Cupbycup.set_add_on(
                        list_addon[int(selec_addon)], (priceOfaddon(readad)[index_selec])
                    )
                    if (len(Cupbycup.add_on) >= (len(list_addon)-1)) :
                        break
                except: 
                    print(" ERROR: Invalid input!")
                    continue
            print(Cupbycup.__repr__())
            classofname.add_ordered_coffee(Cupbycup)
        if customer is None:
            customers.append(classofname)

        print(classofname.receipt())


runStarBUGcafe_main()