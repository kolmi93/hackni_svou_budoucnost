alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, schift_number):
    schifted_text = ""
    for one_character in message:
        if one_character != " ":
            index = alphabet.index(one_character)
            new_index = index + schift_number
            schifted_text += alphabet[new_index]
    print(f"Váš šifrovaný text zní: {schifted_text}.")

def decode(message, schift_number):
    normal_text = ""
    for one_character in message:
        if one_character != " ":
            index_2 = alphabet.index(one_character)
            new_index_2 = index_2 - schift_number
            normal_text += alphabet[new_index_2]
    print(f"Váš dešifrovaný text zní: {normal_text}.")

choice = input("Napište 'encode' pokud chcete text zašifrovat a 'decode' pokud chcete text odšifrovat.\n")
message = input("Napiště text, který chcete přeložit.\n").lower()
schift_number = int(input("O kolik písmen se má Váš text posunout?\n"))

if choice == "encode":
    encode(message, schift_number)
    is_valid = True
elif choice == "decode":
    decode(message, schift_number)
    is_valid = True
else:
    print("Špatně jste zvolili možnost text 'encode' či 'decode'. Prosím, zkuste to znovu.")
    is_valid = False

while not is_valid:
    new_choice = input("Napište 'encode' pokud chcete text zašifrovat a 'decode' pokud chcete text odšifrovat.\n ")
    if new_choice == "encode":
        is_valid = True
        encode(new_choice)
    elif new_choice == "decode":
        is_valid = True
        encode(new_choice)
    else:
        is_valid = False
        print("Neplatný požadavek. Prosím, zkuste to znovu.")

next = input("Chcete pokračovat? Napiště 'ano' nebo 'ne'.\n")
while next == "ano":
    choice = input("Napište 'encode' pokud chcete text zašifrovat a 'decode' pokud chcete text odšifrovat.\n")
    message = input("Napiště text, který chcete přeložit.\n").lower()
    schift_number = int(input("O kolik písmen se má Váš text posunout?\n"))
    if choice == "encode":
        encode(message, schift_number)
        is_valid = True
    elif choice == "decode":
        decode(message, schift_number)
        is_valid = True
    else:
        print("Neplatný požadavek. Prosím, zkuste to znovu.")
        is_valid = False
else:
    exit()