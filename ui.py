from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#ffffff"
RED = "#991203"
GREEN = "#018a06"
FONT_1 = ("Helvetica", 12, "normal")
FONT_2 = ("Arial", 20, "italic")


class UInterface:
    def __init__(self, title, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title(title)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.lbl_score = Label(text="Score: 0", font=FONT_1, fg=WHITE, bg=THEME_COLOR, highlightthickness=0)
        self.lbl_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.text = self.canvas.create_text(
            150,
            125,
            text="text",
            font=FONT_2,
            width=240,
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.btn_ok = Button(text="YES",
                             bg=GREEN,
                             command=lambda: self.submit("True"),
                             width=6, height=3,
                             highlightthickness=0
                             )
        self.btn_ok.grid(column=0, row=2)
        self.btn_nok = Button(text="NO", command=lambda: self.submit("False"), width=6, height=3, highlightthickness=0,
                              bg=RED)
        self.btn_nok.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.text, text=self.quiz.next_question())

    def submit(self, answer):
        is_correct = self.quiz.check_answer(answer)
        if is_correct:
            bg_color = GREEN
        else:
            bg_color = RED

        self.flash_canvas_bg(bg_color)
        self.window.after(1000, self.flash_canvas_bg, WHITE)

        self.lbl_score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.text, text="You have answered all questions!")
            self.btn_ok.config(state=DISABLED)
            self.btn_nok.config(state=DISABLED)

    def flash_canvas_bg(self, bg_color):
        self.canvas.config(bg=bg_color)
