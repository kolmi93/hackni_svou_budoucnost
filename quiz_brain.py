class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_li = q_list

    def next_question(self):
        current_question = self.question_li[self.question_number]
        # vytvoří samostatnou otázku bez odpovědi
        self.question_number += 1
        # bude posouvat pokládanou otázku o +1
        used_answer = input(f"Otázka č. {self.question_number}: {current_question.text}. (True/False): ")
        self.check_answer(used_answer, current_question.answer)
        # kontrola odpovědí - dále v def check_answer

    def has_question(self):
        if self.question_number < len(self.question_li):
            return True
        return False
    

    def check_answer(self, user_a, correct_a):
        if user_a.lower() == correct_a.lower():
            print("Uhádli jste!")
            self.score += 1
        else:
            print(f"Špatná odpověd. Správná odpověď je: {correct_a}.")
            print(f"Vaše scóre je: {self.score}/{self.question_number}.")
    
    def still_question(self):
        if self.question_number < len(self.question_li):
            return True
        return False
    
