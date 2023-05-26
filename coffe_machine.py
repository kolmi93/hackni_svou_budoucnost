from coffe_machine_data import MENU
from coffe_machine_data import resources

choice = input("Co byste si dal/a? Espresso, latte nebo cappuccino?\n").lower()

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

if choice == "espresso" or choice == "cappuccino" or choice == "latte":
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    if resources["water"] > 0 or resources["milk"] > 0  or resources["milk"] > 0:
        print(f"Zbývá {water} ml vody, {milk} ml mléka a {coffee} g kávy.\n")
    else:
        print("Vámi požadovaný nápoj nelze připravit z důvodu nedostatku ingrediencí.\n")
        exit()
    price = int(MENU[choice]["cost"])
    print(f"Cena {choice} je {price},- Kč.\n")
    print("Nyní je třeba zaplatit.\n")
    k_1 = int(input("Kolik kusů 1,- Kč vložíte? "))
    k_2 = int(input("Kolik kusů 2,- Kč vložíte? "))
    k_5 = int(input("Kolik kusů 5,- Kč vložíte? "))
    k_10 = int(input("Kolik kusů 10,- Kč vložíte? "))
    k_20 =  int(input("Kolik kusů 20,- Kč vložíte? "))
    k_50 = int(input("Kolik kusů 50,- Kč vložíte? "))
    total = int((k_1*1)+(k_2*2)+(k_5*5)+(k_10*10)+(k_20*20)+(k_50*50))
    if total == price:
        print("Vloži/a jste dostatek peněz. Nyní se Vám začne nápoj připravovat. Dobrou chuť.")
    elif total > price:
        print(f"Vložil/a jste dostatek peněz. Vrátíme Vám {(total-price)},- Kč. Nyní se Vám začne nápoj připravovat. Dobrou chuť.")
    elif total < price:
        print(f"Zbývá Vám ještě zaplatit {(price-total)},- Kč.")
        i_valid = False
        while not i_valid:
            k_11 = int(input("Kolik kusů 1,- Kč vložíte? "))
            k_21 = int(input("Kolik kusů 2,- Kč vložíte? "))
            k_51 = int(input("Kolik kusů 5,- Kč vložíte? "))
            k_101 = int(input("Kolik kusů 10,- Kč vložíte? "))
            k_201 =  int(input("Kolik kusů 20,- Kč vložíte? "))
            k_501 = int(input("Kolik kusů 50,- Kč vložíte? "))
            total_1 = int((k_11*1)+(k_21*2)+(k_51*5)+(k_101*10)+(k_201*20)+(k_501*50))
            if total_1 == price:
                print("Vloži/a jste dostatek peněz. Nyní se Vám začne nápoj připravovat. Dobrou chuť.")
                i_valid = True
                break
            elif total_1 > price:
                print(f"Vloži/a jste dostatek peněz. Vrátíme Vám {(total_1-price)},- Kč. Nyní se Vám začne nápoj připravovat. Dobrou chuť.")
                i_valid = True
                break
            elif total_1 < price:
                print(f"Zbývá Vám ještě zaplatit {(price-total_1)},- Kč.")
                i_valid = False
elif choice == "report":
    print(f"Stav zásob: voda - {water}, mléko - {milk}, káva - {coffee}.")
else:
    print("Vámi požadovaný drink neumíme vyrobit.\n")
    is_valid = False
    while not is_valid:
        again = input("Chcete si vybrat nápoj znovu? Ano či ne?\n").lower()
        if again == "ano":
            new_choice = input("Co byste si dal/a? Espresso, latte nebo cappuccino?\n").lower()
            if new_choice == "espresso" or new_choice == "cappuccino" or new_choice == "latte":
                resources["water"] -= MENU[new_choice]["ingredients"]["water"]
                resources["milk"] -= MENU[new_choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[new_choice]["ingredients"]["coffee"]
                if resources["water"] > 0 or resources["milk"] > 0  or resources["milk"] > 0:
                    print(f"Zbývá {water} ml vody, {milk} ml mléka a {coffee} g kávy.\n")
                else:
                    print("Vámi požadovaný nápoj nelze připravit z důvodu nedostatku ingrediencí.\n")
                    exit()
                new_price = int(MENU[new_choice]["cost"])
                is_valid = True
                print(f"Cena {new_choice} je {new_price},- Kč.\n")
                print("Nyní je třeba zaplatit.\n")
                k_12 = int(input("Kolik kusů 1,- Kč vložíte? "))
                k_22 = int(input("Kolik kusů 2,- Kč vložíte? "))
                k_52 = int(input("Kolik kusů 5,- Kč vložíte? "))
                k_102 = int(input("Kolik kusů 10,- Kč vložíte? "))
                k_202 =  int(input("Kolik kusů 20,- Kč vložíte? "))
                k_502 = int(input("Kolik kusů 50,- Kč vložíte? "))
                total_2 = int((k_12*1)+(k_22*2)+(k_52*5)+(k_102*10)+(k_202*20)+(k_502*50))
                if total_2 == new_price:
                    print("Vloži/a jste dostatek peněz. Nyní se Vám začne nápoj připravovat. Dobrou chuť.")
                elif total_2 > new_price:
                    print(f"Vloži/a jste dostatek peněz. Vrátíme Vám {(total_2-new_price)},- Kč. Nyní se Vám začne nápoj připravovat. Dobrou chuť.")
                elif total_2 < new_price:
                    print(f"Zbývá Vám ještě zaplatit {(new_price-total_2)},- Kč.")
                    i_valid = False
                    while not i_valid:
                        k_13 = int(input("Kolik kusů 1,- Kč vložíte? "))
                        k_23 = int(input("Kolik kusů 2,- Kč vložíte? "))
                        k_53 = int(input("Kolik kusů 5,- Kč vložíte? "))
                        k_103 = int(input("Kolik kusů 10,- Kč vložíte? "))
                        k_203 =  int(input("Kolik kusů 20,- Kč vložíte? "))
                        k_503 = int(input("Kolik kusů 50,- Kč vložíte? "))
                        total_3 = ((k_13*1)+(k_23*2)+(k_53*5)+(k_103*10)+(k_203*20)+(k_503*50))
                        if total_3 == new_price:
                            print("Vloži/a jste dostatek peněz. Nyní se Vám začne nápoj připravovat. Dobrou chuť.")
                            i_valid = True
                        elif total_3 == new_price:
                            print("Vloži/a jste dostatek peněz. Nyní se Vám začne nápoj připravovat. Dobrou chuť.")
                            i_valid = True
                        elif total_3 > new_price:
                            print(f"Vloži/a jste dostatek peněz. Vrátíme Vám {(total_3-new_price)},- Kč. Nyní se Vám začne nápoj připravovat. Dobrou chuť.")
                            i_valid = True
                        elif total_3 > new_price:
                            print(f"Vloži/a jste dostatek peněz. Vrátíme Vám {(total_3-new_price)},- Kč. Nyní se Vám začne nápoj připravovat. Dobrou chuť.")
                            i_valid = True
                        elif total_3 < new_price:
                            print(f"Zbývá Vám ještě zaplatit {(new_price-total_3)},- Kč.")
                            i_valid = False
                        else:
                            print(f"Zbývá Vám ještě zaplatit {(new_price-total_3)},- Kč.")
                            i_valid = False
                elif choice == "report":
                    is_valid = True
                    print(f"Stav zásob: voda - {water}, mléko - {milk}, káva - {coffee}.")
                    break
                else:
                    is_valid = False
        else:
            print("Budeme se těšit na Vaši další návštěvu. Nashledanou.")