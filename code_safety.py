name = input("Zadejte své jméno:\n")
code = input("Zadejte své heslo:\n")
code2 = input("Zadejte znovu své heslo:\n")

if code!=code2:
    print("Heslo, které jste zadali není stejné.")
    if len(code) >= 8:
        print("Vaše heslo je bezpečné.")
    else:
        print("Vaše heslo není bezpečné.")
else:
    print("Hesla jsou stejná.")