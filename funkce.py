import random
words = ["harry", "hermiona", "albus", "ronald"]
random_words = words[random.randint(0, len(words))]

hidden_word = []
for one_letter in random_words:
    hidden_word.append("_")

printed_word = ""
for one_letter in hidden_word:
    printed_word += one_letter
print(printed_word)

while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno.\n").lower()
    for index in range(0, len(random_words)):
        if guess == random_words[index]:
            hidden_word[index] = guess
    if "_" not in hidden_word:
        print("Vyhráli jste.")

printed_word = ""
for one_letter in hidden_word:
    printed_word += one_letter
print(printed_word)

if "_" not in hidden_word:
        print("Vyhráli jste.")