class Robot:
    
    #constructor = speciální funkce. Vyvolá se, hned, jak funkci použijeme.
    def __init__(self, battery, hand_lenght):
        self.battery = battery
        self.hand_lenght = hand_lenght
        #self.safety_check = 365
        self.tasks_to_check = 1000
        # == DEFAULTNÍ HODNOTA - pro všechny roboty stejný, není třeba vypisovat samostatně ke každému robotovi.

    def move_forward (self):
        print("Robot udělal krok vzpřed.")
        self.tasks_to_check -= 1
        print(f"Zbývá {self.tasks_to_check} úkonů do kontroly.")
    
    def move_backwards (self):
        print("Robot udělal krok vzad.")
        self.tasks_to_check -= 1
        print(f"Zbývá {self.tasks_to_check} úkonů do kontroly.")

robot_1 = Robot(24,0.6)
# robot_1.baterie = 24 - už tam být nemusí, už je to nahoře v robot_1
# robot_1.delka_rukou = 0.6
robot_2 = Robot(48, 0.5)
robot_3 = Robot(72, 0.7)
robot_4 = Robot(96, 0.6)

print(f"Robot č. 1: Výdrž baterie: {robot_1.battery} hodin.")
print(f"Robot č. 1: Délka rukou: {robot_1.hand_lenght} m.")
print(f"Robot č. 1: Do bezpečnostní kontroly zbývá: {robot_1.tasks_to_check} úkonů.")
#print(f"Robot č. 2: Výdrž baterie: {robot_2.battery} hodin.")
#print(f"Robot č. 2: Délka rukou: {robot_2.hand_lenght} m.")
#print(f"Robot č. 2: Do bezepčnostní kontroly zbývá: {robot_1.safety_check} dnů.")
#print(f"Robot č. 3: Výdrž baterie: {robot_3.battery} hodin.")
#print(f"Robot č. 3: Délka rukou: {robot_3.hand_lenght} m.")
#print(f"Robot č. 3: Do bezepčnostní kontroly zbývá: {robot_1.safety_check} dnů.")
#print(f"Robot č. 4: Výdrž baterie: {robot_4.battery} hodin.")
#print(f"Robot č. 4: Délka rukou: {robot_4.hand_lenght} m.")
#print(f"Robot č. 4: Do bezepčnostní kontroly zbývá: {robot_1.safety_check} dnů.")
robot_1.move_backwards()
robot_1.move_forward()
robot_1.move_backwards()
robot_1.move_backwards()
robot_1.move_backwards()
robot_1.move_forward()
print(f"Robot č. 1: Do bezpečnostní kontroly zbývá: {robot_1.tasks_to_check} úkonů.")
