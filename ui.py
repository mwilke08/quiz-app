from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=40, pady=40, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=1)

        self.my_canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.my_canvas.create_text(150, 125, text="Test Text",
                                                        fill=THEME_COLOR,
                                                        width=280,
                                                        font=("Arial", 20, "italic"))
        self.my_canvas.grid(row=1, column=0, columnspan=2, pady=15)

        true_btn_image = PhotoImage(file="./images/true.png")
        false_btn_image = PhotoImage(file="./images/false.png")
        self.true_btn = Button(image=true_btn_image, highlightthickness=0,
                               command=self.true_pressed)
        self.false_btn = Button(image=false_btn_image, highlightthickness=0,
                                command=self.false_pressed)
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.enable_buttons()
            self.my_canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.my_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.disable_buttons()
            self.my_canvas.config(bg="white")
            self.my_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def disable_buttons(self):
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")

    def enable_buttons(self):
        self.true_btn.config(state="active")
        self.false_btn.config(state="active")

    def give_feedback(self, is_right: bool):
        if is_right:
            self.disable_buttons()
            self.my_canvas.config(bg="green")
        else:
            self.disable_buttons()
            self.my_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

