from tkinter import *
from quiz_brain import QuizBrain

TEXT_FONT = ('arial', 20, 'italic')
THEME_COLOR = "#375362"


class QuizUi:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Computer Quiz")
        self.window.config(width=400, height=800, bg=THEME_COLOR, padx=20)
        self.score = Label(text=f'Score: {self.quiz.score}', pady=20, padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, bg='white')
        self.question_text = self.canvas.create_text(145, 125, text=f"", font=TEXT_FONT, width=280, fill='black')
        self.correct_image = PhotoImage(file='images/true.png')
        self.incorrect_image = PhotoImage(file='images/false.png')
        self.correct_button = Button(image=self.correct_image, highlightthickness=0, command=self.answer_true)
        self.incorrect_button = Button(image=self.incorrect_image, highlightthickness=0, command=self.answer_false)
        self.score.grid(column=2, row=1)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=(0, 20))
        self.correct_button.grid(column=1, row=3, pady=(0, 20))
        self.incorrect_button.grid(column=2, row=3, pady=(0, 20))

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.correct_button.config(state='disabled')
            self.incorrect_button.config(state='disabled')

    def answer_true(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)
        self.score.config(text=f'Score: {self.quiz.score}')

    def answer_false(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)
        self.score.config(text=f'Score: {self.quiz.score}')

    def give_feedback(self, is_right):
        if is_right: self.canvas.config(bg='green')
        if not is_right: self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
