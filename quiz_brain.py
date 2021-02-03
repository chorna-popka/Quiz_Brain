class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.current_question = None
        self.score = 0
        self.question_bank = question_bank

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        self.current_question = self.question_bank[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.question}"

    def check_answer(self, answer):
        if answer.lower() == self.current_question.correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

