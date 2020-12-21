from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
QUESTION_FONT = ('Arial', 20, 'italic')

class UserInterface():
    def __init__(self, quizbrain : QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=False)
        self.question_text = self.canvas.create_text(150, 125, text='test', font=QUESTION_FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.true_btn = Button(image=true_img, highlightthickness=False, command=self.say_yes)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(image=false_img, highlightthickness=False, command=self.say_no)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_text.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You\'ve reached the end of questions')
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def say_yes(self):
        is_right = self.quiz.check_answer('True')
        self.check_is_right(is_right)

    def say_no(self):
        is_right = self.quiz.check_answer('False')
        self.check_is_right(is_right)

    def check_is_right(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

