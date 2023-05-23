import random
from test import stages

print("Vítejte ve hře hádání postav z filmu Harry Potter. Vaším úkolem je...")

#generování náhodného slova
words = ["harry", "hermiona", "albus", "ronald"]
random_words = words[random.randint(0, 3)]

#generování podtržítek
hidden_word = []
for one_letter in random_words:
    hidden_word.append("_")

#životy
lives = 6
print(stages[lives])

#vypsání slova s podtržítky v normální podobě
printed_word = ""
for one_letter in hidden_word:
    printed_word += one_letter
print(printed_word)

while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno.\n").lower()
    for index in range(0, len(random_words)):
        if guess == random_words[index]:
            hidden_word[index] = guess

#kontrola životů a vypsání
    if guess not in random_words:
        lives -=1
        print(stages[lives])
    print(f"Počet Vašich životů je {lives}.")
    if lives == 0:
        print("Prohráli jste!")     
        break

    if "_" not in hidden_word:
        print("Vyhráli jste.")

#vypsání slova s podtržítky v normální podobě
    printed_word = ""
    for one_letter in hidden_word:
        printed_word += one_letter
    print(printed_word)

    if "_" not in hidden_word:
            print("Vyhráli jste.")