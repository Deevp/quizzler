THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
from tkinter import *
from unittest import skip
from quiz_brain import QuizBrain

class QuizUI:
    def __init__(self):
        try: 
            self.window
        except:
            self.window = Tk()
        self.window.title('Quizler')
        self.window.config(bg=THEME_COLOR)
        self.window.minsize(width=340, height=500)
        quiz = QuizBrain()
        self.score = 0
        self.quiz = quiz

        self.score_label = Label(text=f'Score: {self.score}', bg=THEME_COLOR, fg='white', highlightthickness=0)
        self.score_label.grid(row=0, column=1, padx=20,pady=20)

        self.canvas = Canvas(highlightthickness=0, width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, text=f'f', font=FONT, fill=THEME_COLOR, width=290)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20,pady=20)
        ok_image = PhotoImage(file='images/true.png')
        self.ok_button = Button(image=ok_image, highlightthickness=0, command=self.ok_pressed)
        self.ok_button.grid(row=2, column=0, padx=20,pady=20)

        x_image = PhotoImage(file='images/false.png')
        self.x_button = Button(image=x_image, highlightthickness=0, command=self.x_pressed)
        self.x_button.grid(row=2, column=1, padx=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.ok_button["state"] = "normal"
        self.x_button["state"] = "normal"
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.game_over()

    def ok_pressed(self):
        if self.quiz.check_answer("True"):
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.ok_button["state"] = 'disabled'
        self.x_button["state"] = 'disabled'

        self.window.after(500, self.get_next_question)

    def x_pressed(self):
        if self.quiz.check_answer("False"):
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.ok_button["state"] = 'disabled'
        self.x_button["state"] = 'disabled'
        self.window.after(500, self.get_next_question)
        
    def game_over(self):
        for widjets in self.window.winfo_children():
            widjets.destroy()
        self.game_over_label = Label(text='GAME OVER', font=("Courier", 40, "bold"), fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.game_over_label.pack(ipadx=20, ipady=20)
        self.final_score = Label(text=f'Final Score: {self.quiz.score}', font=("Courier", 26, "bold"), fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.final_score.pack(ipadx=20, ipady=20)
        self.play_again_button = Button(text="Play Again", command=self.game_start)
        self.play_again_button.pack(ipadx=20, ipady=20)
    
    def game_start(self):
        for widjets in self.window.winfo_children():
            widjets.destroy()
        self.__init__()
