import html


class Question:
    def __init__(self, el):
        self.category = el['category']
        self.type = el['type']
        self.difficulty = el['difficulty']
        self.question = html.unescape(el['question'])
        self.correct_answer = el['correct_answer']
        self.incorrect_answers = el['incorrect_answers']
