from tkinter import *
import random

class MATH_GAME:
    def __init__(self):
        self.root = Tk()
        self.root.title('Math Game')
        self.root.geometry('400x400')
        self.root.resizable(False, False)
        self.canvas = Canvas(width=200, height=5)
        self.minutes = 0
        self.seconds = 20
        self.player_correct_score = 0
        self.player_incorrect_score = 0
        self.enter_box_check = []
        
    def make_root(self):
        self.root.configure(bg='blue')
        self.math_game_button_frame = Frame(self.root)
        self.math_game_button = Label(self.math_game_button_frame, text='Math Game', font=('Helvetica bold', 30))
        self.math_game_button_frame.pack(pady=10)
        self.math_game_button.pack()
        self.start_game_button_frame = Frame(self.root)
        self.start_game_button = Button(self.start_game_button_frame, text='Click to Start Game', font=('Helvetica bold', 15), command=self.start_game)
        self.start_game_button_frame.pack(pady=20)
        self.start_game_button.pack()
        
    def start_game(self):
        self.root.configure(bg='green')
        self.math_game_button_frame.pack_forget()
        self.start_game_button_frame.pack_forget()
        self.game_started_button_frame = Frame(self.root)
        self.game_started_button = Label(self.game_started_button_frame)
        self.game_started_button_frame.pack(pady=20)
        self.game_started_button.pack()

        self.play_game()
        self.update_timer()

        
    def update_timer(self):
        try:
            self.minutes_format = f'{self.minutes:02d}'
            self.seconds_format = f'{self.seconds:02d}'
            self.game_started_button.config(text=self.minutes_format + ':' + self.seconds_format, font=('Helvetica bold', 20))
            self.minutes = int(self.minutes_format)
            self.seconds = int(self.seconds_format)
            
            if self.minutes > 0 and self.seconds == 0:
                self.minutes -= 1
                self.seconds = 59
                
            elif self.minutes > -1 and self.seconds != 0:
                self.seconds -= 1
                
            else:
                self.game_over()
                
            
            self.game_started_button.after(1000, self.update_timer)
        except:
            print('The Game Is Over')

    def play_game(self):
        self.which_sign_for_game = random.randint(1, 2)
        self.which_number_player_will_guess = random.randint(1, 3)
        if self.which_sign_for_game == 1:
            self.x = random.randint(1, 10)
            self.y = random.randint(1, 10)
        elif self.which_sign_for_game == 2:
            self.x = random.randint(1, 50)
            self.y = random.randint(1, 50)            
        self.product_result = self.x * self.y
        self.add_result = self.x + self.y
        self.player_multiply_entry_box_frame1 = Frame(self.root)
        self.first_entry_multiply_number = Entry(self.player_multiply_entry_box_frame1, width=2, font=('Helvetica bold', 40), justify=RIGHT)
        self.player_multiply_entry_box_frame2 = Frame(self.root, width= 7, bg='green')
        self.multiply_sign_for_second_entry = Label(self.player_multiply_entry_box_frame2, width=1, text='X', font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        #self.subtract_sign_for_second_entry = Label(self.player_subtract_entry_box_frame2, width=1, text='-', font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        #self.divide_sign_for_second_entry = Label(self.player_multiply_entry_box_frame2, width=1, text='X', font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.second_entry_multiply_number = Entry(self.player_multiply_entry_box_frame2, width=2, font=('Helvetica bold', 40), justify=RIGHT)
        self.canvas.create_line(40,5,190,5,width=2)
        self.player_multiply_entry_box_frame3 = Frame(self.root)
        self.third_entry_multiply_number = Entry(self.player_multiply_entry_box_frame3, width=3, font=('Helvetica bold', 40), justify=RIGHT)
        self.first_multiply_text_frame = Frame(self.root, bg='green')
        self.first_multiply_text_number = Label(self.first_multiply_text_frame, width=2, text=self.x, font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.second_multiply_text_frame = Frame(self.root, bg='green')
        self.second_multiply_text_number = Label(self.second_multiply_text_frame, width=4, text=f'X  {self.y}', font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.third_multiply_text_frame = Frame(self.root, bg='green')
        self.third_multiply_text_number = Label(self.third_multiply_text_frame, width=3, text=self.product_result, font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.player_add_entry_box_frame1 = Frame(self.root)
        self.first_entry_add_number = Entry(self.player_add_entry_box_frame1, width=2, font=('Helvetica bold', 40), justify=RIGHT)
        self.player_add_entry_box_frame2 = Frame(self.root, width= 7, bg='green')
        self.add_sign_for_second_entry = Label(self.player_add_entry_box_frame2, width=1, text='+', font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.second_entry_add_number = Entry(self.player_add_entry_box_frame2, width=2, font=('Helvetica bold', 40), justify=RIGHT)
        self.canvas.create_line(40,5,190,5,width=2)
        self.player_add_entry_box_frame3 = Frame(self.root)
        self.third_entry_add_number = Entry(self.player_add_entry_box_frame3, width=3, font=('Helvetica bold', 40), justify=RIGHT)
        self.first_add_text_frame = Frame(self.root, bg='green')
        self.first_add_text_number = Label(self.first_add_text_frame, width=2, text=self.x, font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.second_add_text_frame = Frame(self.root, bg='green')
        self.second_add_text_number = Label(self.second_add_text_frame, width=4, text=f'+  {self.y}', font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        self.third_add_text_frame = Frame(self.root, bg='green')
        self.third_add_text_number = Label(self.third_add_text_frame, width=3, text=self.add_result, font=('Helvetica bold', 40), justify=RIGHT, bg='green')
        
        
        if self.which_sign_for_game == 1:
            if self.which_number_player_will_guess == 1:
                if 1 not in self.enter_box_check:
                    self.enter_box_check.append(1)
                self.player_multiply_entry_box_frame1.pack(anchor='e', padx=15, pady=5)
                self.first_entry_multiply_number.pack()
                self.first_entry_multiply_number.focus_set()
                self.second_multiply_text_frame.pack(anchor='e', padx=10)
                self.second_multiply_text_number.pack()
                self.canvas.pack(anchor='e')
                self.third_multiply_text_frame.pack(anchor='e', padx=15, pady=5)
                self.third_multiply_text_number.pack()
                self.enter_multiply_answer_frame_button_1 = Frame(self.root)
                self.enter_multiply_answer_button_1 = Button(self.enter_multiply_answer_frame_button_1, text='ENTER', command=self.enter_multiply_answer_1)
                self.enter_multiply_answer_frame_button_1.pack(pady=10)
                self.enter_multiply_answer_button_1.pack()
            elif self.which_number_player_will_guess == 2:
                if 2 not in self.enter_box_check:
                    self.enter_box_check.append(2)
                self.first_multiply_text_frame.pack(anchor='e', padx=15, pady=5)
                self.first_multiply_text_number.pack()
                self.player_multiply_entry_box_frame2.pack(anchor='e', padx=5)
                self.second_entry_multiply_number.pack(padx=15, side='right')
                self.second_entry_multiply_number.focus_set()
                self.multiply_sign_for_second_entry.pack(padx=20, side='right')
                self.canvas.pack(anchor='e')
                self.third_multiply_text_frame.pack(anchor='e')
                self.third_multiply_text_number.pack()
                self.enter_multiply_answer_frame_button_2 = Frame(self.root)
                self.enter_multiply_answer_button_2 = Button(self.enter_multiply_answer_frame_button_2, text='ENTER', command=self.enter_multiply_answer_2)
                self.enter_multiply_answer_frame_button_2.pack(pady=10)
                self.enter_multiply_answer_button_2.pack()
            elif self.which_number_player_will_guess == 3:
                if 3 not in self.enter_box_check:
                    self.enter_box_check.append(3)
                self.first_multiply_text_frame.pack(anchor='e', padx=10)
                self.first_multiply_text_number.pack()
                self.second_multiply_text_frame.pack(anchor='e', padx=10)
                self.second_multiply_text_number.pack()
                self.canvas.pack(anchor='e')
                self.player_multiply_entry_box_frame3.pack(anchor='e', padx=15, pady=5)
                self.third_entry_multiply_number.pack()
                self.third_entry_multiply_number.focus_set()
                self.enter_multiply_answer_frame_button_3 = Frame(self.root)
                self.enter_multiply_answer_button_3 = Button(self.enter_multiply_answer_frame_button_3, text='ENTER', command=self.enter_multiply_answer_3)
                self.enter_multiply_answer_frame_button_3.pack(pady=10)
                self.enter_multiply_answer_button_3.pack()
                
        elif self.which_sign_for_game == 2:
            if self.which_number_player_will_guess == 1:
                if 4 not in self.enter_box_check:
                    self.enter_box_check.append(4)
                self.player_add_entry_box_frame1.pack(anchor='e', padx=15, pady=5)
                self.first_entry_add_number.pack()
                self.first_entry_add_number.focus_set()
                self.second_add_text_frame.pack(anchor='e', padx=10)
                self.second_add_text_number.pack()
                self.canvas.pack(anchor='e')
                self.third_add_text_frame.pack(anchor='e', padx=15, pady=5)
                self.third_add_text_number.pack()
                self.enter_add_answer_frame_button_1 = Frame(self.root)
                self.enter_add_answer_button_1 = Button(self.enter_add_answer_frame_button_1, text='ENTER', command=self.enter_add_answer_1)
                self.enter_add_answer_frame_button_1.pack(pady=10)
                self.enter_add_answer_button_1.pack()
            elif self.which_number_player_will_guess == 2:
                if 5 not in self.enter_box_check:
                    self.enter_box_check.append(5)
                self.first_add_text_frame.pack(anchor='e', padx=15, pady=5)
                self.first_add_text_number.pack()
                self.player_add_entry_box_frame2.pack(anchor='e', padx=5)
                self.second_entry_add_number.pack(padx=15, side='right')
                self.second_entry_add_number.focus_set()
                self.add_sign_for_second_entry.pack(padx=20, side='right')
                self.canvas.pack(anchor='e')
                self.third_add_text_frame.pack(anchor='e')
                self.third_add_text_number.pack()
                self.enter_add_answer_frame_button_2 = Frame(self.root)
                self.enter_add_answer_button_2 = Button(self.enter_add_answer_frame_button_2, text='ENTER', command=self.enter_add_answer_2)
                self.enter_add_answer_frame_button_2.pack(pady=10)
                self.enter_add_answer_button_2.pack()
            elif self.which_number_player_will_guess == 3:
                if 6 not in self.enter_box_check:
                    self.enter_box_check.append(6)
                self.first_add_text_frame.pack(anchor='e', padx=10)
                self.first_add_text_number.pack()
                self.second_add_text_frame.pack(anchor='e', padx=10)
                self.second_add_text_number.pack()
                self.canvas.pack(anchor='e')
                self.player_add_entry_box_frame3.pack(anchor='e', padx=15, pady=5)
                self.third_entry_add_number.pack()
                self.third_entry_add_number.focus_set()
                self.enter_add_answer_frame_button_3 = Frame(self.root)
                self.enter_add_answer_button_3 = Button(self.enter_add_answer_frame_button_3, text='ENTER', command=self.enter_add_answer_3)
                self.enter_add_answer_frame_button_3.pack(pady=10)
                self.enter_add_answer_button_3.pack() 
            
                        
    def enter_multiply_answer_1(self):
        try:
            player_guess = int(self.first_entry_multiply_number.get())
            print(player_guess)
            if player_guess == self.x:
                self.player_correct_score +=1
                self.player_multiply_entry_box_frame1.pack_forget()
                self.second_multiply_text_frame.pack_forget()
                self.canvas.pack_forget()
                self.third_multiply_text_frame.pack_forget()
                self.enter_multiply_answer_frame_button_1.pack_forget()
                self.play_game()

            elif player_guess != self.x:
                self.player_incorrect_score += 1
                self.player_multiply_entry_box_frame1.pack_forget()
                self.second_multiply_text_frame.pack_forget()
                self.canvas.pack_forget()
                self.third_multiply_text_frame.pack_forget()
                self.enter_multiply_answer_frame_button_1.pack_forget()
                self.play_game()
        except:
            self.first_entry_multiply_number.delete(0, END)
            
    def enter_multiply_answer_2(self):
        try:
            player_guess = int(self.second_entry_multiply_number.get())
            print(player_guess)
            if player_guess == self.y:
                self.player_correct_score +=1
                self.first_multiply_text_frame.pack_forget()
                self.player_multiply_entry_box_frame2.pack_forget()
                self.canvas.pack_forget()
                self.third_multiply_text_frame.pack_forget()
                self.enter_multiply_answer_frame_button_2.pack_forget()
                self.play_game()
            elif player_guess != self.y:
                self.player_incorrect_score += 1
                self.first_multiply_text_frame.pack_forget()
                self.player_multiply_entry_box_frame2.pack_forget()
                self.canvas.pack_forget()
                self.third_multiply_text_frame.pack_forget()
                self.enter_multiply_answer_frame_button_2.pack_forget()
                self.play_game()
        except:
            self.second_entry_multiply_number.delete(0, END)
        
    def enter_multiply_answer_3(self):
        try:
            player_guess = int(self.third_entry_multiply_number.get())
            print(player_guess)
            if player_guess == self.product_result:
                self.player_correct_score +=1
                self.first_multiply_text_frame.pack_forget()
                self.second_multiply_text_frame.pack_forget()
                self.canvas.pack_forget()
                self.player_multiply_entry_box_frame3.pack_forget()
                self.enter_multiply_answer_frame_button_3.pack_forget()
                self.play_game()
            elif player_guess != self.product_result:
                self.player_incorrect_score += 1
                self.first_multiply_text_frame.pack_forget()
                self.second_multiply_text_frame.pack_forget()
                self.canvas.pack_forget()
                self.player_multiply_entry_box_frame3.pack_forget()
                self.enter_multiply_answer_frame_button_3.pack_forget()
                self.play_game()
            
        except:
            self.third_entry_multiply_number.delete(0, END)
            
    def enter_add_answer_1(self):
        try:
            player_guess = int(self.first_entry_add_number.get())
            print(player_guess)
            if player_guess == self.x:
                self.player_correct_score +=1
                self.player_add_entry_box_frame1.pack_forget()
                self.second_add_text_frame.pack_forget()
                self.canvas.pack_forget()
                self.third_add_text_frame.pack_forget()
                self.enter_add_answer_frame_button_1.pack_forget()
                self.play_game()

            elif player_guess != self.x:
                self.player_incorrect_score += 1
                self.player_add_entry_box_frame1.pack_forget()
                self.second_add_text_frame.pack_forget()
                self.canvas.pack_forget()
                self.third_add_text_frame.pack_forget()
                self.enter_add_answer_frame_button_1.pack_forget()
                self.play_game()

        except:
            self.first_entry_add_number.delete(0, END)
            
    def enter_add_answer_2(self):
        try:
            player_guess = int(self.second_entry_add_number.get())
            print(player_guess)
            if player_guess == self.y:
                self.player_correct_score +=1
                self.first_add_text_frame.pack_forget()
                self.player_add_entry_box_frame2.pack_forget()
                self.canvas.pack_forget()
                self.third_add_text_frame.pack_forget()
                self.enter_add_answer_frame_button_2.pack_forget()
                self.play_game()
            elif player_guess != self.y:
                self.player_incorrect_score += 1
                self.first_add_text_frame.pack_forget()
                self.player_add_entry_box_frame2.pack_forget()
                self.canvas.pack_forget()
                self.third_add_text_frame.pack_forget()
                self.enter_add_answer_frame_button_2.pack_forget()
                self.play_game()
                
        except:
            self.second_entry_add_number.delete(0, END)
        
    def enter_add_answer_3(self):
        try:
            player_guess = int(self.third_entry_add_number.get())
            print(player_guess)
            if player_guess == self.add_result:
                self.player_correct_score +=1
                self.first_add_text_frame.pack_forget()
                self.second_add_text_frame.pack_forget()
                self.canvas.pack_forget()
                self.player_add_entry_box_frame3.pack_forget()
                self.enter_add_answer_frame_button_3.pack_forget()
                self.play_game()
            elif player_guess != self.add_result:
                self.player_incorrect_score += 1
                self.first_add_text_frame.pack_forget()
                self.second_add_text_frame.pack_forget()
                self.canvas.pack_forget()
                self.player_add_entry_box_frame3.pack_forget()
                self.enter_add_answer_frame_button_3.pack_forget()
                self.play_game()
        except:
            self.third_entry_add_number.delete(0, END)
            
        
    def game_over(self):
        self.root.configure(bg='red')
        self.player_multiply_entry_box_frame1.pack_forget()
        self.player_multiply_entry_box_frame2.pack_forget()
        self.multiply_sign_for_second_entry.pack_forget()
        self.canvas.pack_forget()
        self.player_multiply_entry_box_frame3.pack_forget()
        self.first_multiply_text_frame.pack_forget()
        self.second_multiply_text_frame.pack_forget()
        self.third_multiply_text_frame.pack_forget()
        self.player_add_entry_box_frame1.pack_forget()
        self.player_add_entry_box_frame2.pack_forget()
        self.add_sign_for_second_entry.pack_forget()
        self.canvas.pack_forget()
        self.player_add_entry_box_frame3.pack_forget()
        self.first_add_text_frame.pack_forget()
        self.second_add_text_frame.pack_forget()
        self.third_add_text_frame.pack_forget()
        self.game_started_button_frame.pack_forget()
        self.math_game_button_frame.pack_forget()
        self.start_game_button_frame.pack_forget()
        if 1 in self.enter_box_check:
            self.enter_multiply_answer_frame_button_1.pack_forget()
        if 2 in self.enter_box_check:
            self.enter_multiply_answer_frame_button_2.pack_forget()
        if 3 in self.enter_box_check:
            self.enter_multiply_answer_frame_button_3.pack_forget()
        if 4 in self.enter_box_check:
            self.enter_add_answer_frame_button_1.pack_forget()
        if 5 in self.enter_box_check:
            self.enter_add_answer_frame_button_2.pack_forget()
        if 6 in self.enter_box_check:
            self.enter_add_answer_frame_button_3.pack_forget()
        self.root.configure(bg='red')
        self.game_over_button_frame = Frame(self.root)
        self.game_over_button = Label(self.game_over_button_frame, text='GAME OVER', font=('Helvetica bold', 30))
        self.game_over_button_frame.pack(pady=30)
        self.game_over_button.pack()
        self.player_correct_score_frame = Frame(self.root)
        self.player_correct_score_button = Label(self.player_correct_score_frame, text=f'Your Correct Score: {self.player_correct_score} Correct', font=('Helvetica bold', 14))
        self.player_correct_score_frame.pack(pady=30)
        self.player_correct_score_button.pack()
        self.player_incorrect_score_frame = Frame(self.root)
        self.player_incorrect_score_button = Label(self.player_incorrect_score_frame, text=f'Your Incorrect Score: {self.player_incorrect_score} Incorrect', font=('Helvetica bold', 14))
        self.player_incorrect_score_frame.pack(pady=30)
        self.player_incorrect_score_button.pack()
        
        self.root.mainloop()


def main():
    first_try = MATH_GAME()
    the_return = first_try.make_root()


if __name__ == '__main__':
    main()
        