import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Vítejte u hry kámen, nůžky papír.")
choice = input("Vyberte si kámen, nůžky nebo papír.\n")

if choice == "kámen":
    print("Zvolili jste si kámen.\n" + rock)
elif choice == "nůžky":
    print("Zvolili jste si nůžky.\n" + scissors)
else: 
    print("Zvolili jste si papír.\n" + paper)

list = [rock, paper, scissors]
pc_choice = random.choice(list)

print(f"Počítač si zvolil:\n {pc_choice}")

if choice == "kámen" and pc_choice == rock:
    print("Remíza")
elif choice == "nůžky" and pc_choice == scissors:
    print("Remíza")
elif choice == "papír" and pc_choice == paper:
    print("Remíza")
elif choice == "kámen" and pc_choice == scissors:
    print("Vyhrál si.")
elif choice == "nůžky" and pc_choice == rock:
    print("Prohrál si.")
elif choice == "kámen" and pc_choice == paper:
    print("Prohrál si.")
elif choice == "papír" and pc_choice == rock:
    print("Vyhrál si.")
elif choice == "nůžky" and pc_choice == paper:
    print("Vyhrál si.")
elif choice == "papír" and pc_choice == scissors:
    print("Prohrál si.")