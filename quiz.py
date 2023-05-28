from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []

for one_question in question_data:
    question_t = one_question["text"]
    # vyprintuje z question data otázky
    question_a = one_question["answer"]
    # vyprintuje z question data odpovědi
    new_question = Question(question_t, question_a)
    # posílá do question_model data do Class Question
    question_list.append(new_question)
    # uloží data do nováho seznamu question_listu

quiz = QuizBrain(question_list)
quiz.next_question()
while quiz.has_question() == True:
    quiz.next_question()
    # jakmile budou všechny otázky vyčerpány, vypne se
print("Dokončili jste kvíz.")
print(f"Vaš celkové scóre je {quiz.score}/{quiz.question_number}.")