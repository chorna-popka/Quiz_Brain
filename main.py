from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import UInterface


question_bank = []

for el in question_data:
    question_bank.append(Question(el))

quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

ui = UInterface("Quizzzy", quiz)

print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")