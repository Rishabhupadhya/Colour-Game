from tkinter import *
import tkinter.font as font
import random



root = Tk()
root.title("Colour Game")
root.geometry('600x300')
root.resizable(False,False)


def startGame():
    global displayed_word_color

    if(timer == 60):
        startCountDown()
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text=random.choice(colors), fg=displayed_word_color)
        e1.bind('<Return>', displayNextWord)


def resetGame():
    global timer, score, displayed_word_color
    timer = 60
    score = 0
    displayed_word_color = ''
    game_score.config(text = "Your Score : " + str(score))
    display_words.config(text = '')
    time_left.config(text="Game Ends in : -")
    e1.delete(0, END)


def startCountDown():
    global timer
    if(timer >= 0):
        time_left.config(text = "Game Ends in : " + str(timer) + "s")
        timer -= 1
        time_left.after(1000,startCountDown)
        if (timer == -1):
            time_left.config(text="Game Over!!!")


def displayNextWord(event):
    global displayed_word_color
    global score
    if(timer > 0):
        if(displayed_word_color == e1.get().lower()):
            score += 1
            game_score.config(text = "Your Score : " + str(score))
        e1.delete(0, END)
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text = random.choice(colors), fg = displayed_word_color)

def exit():
    root.destroy()

app_font = font.Font(family='Helvetica', size = 12)

game_desp = "Game Description: Enter the color of the words displayed below. \n And Keep in mind not to enter the word text itself"
myFont = font.Font(family='Helvetica')

game_description = Label(root, text = game_desp, font = app_font, fg= "grey")
game_description.pack()





colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]

timer = 60
score = 0
displayed_word_color = ''

game_score = Label(root, text = "Your Score : " + str(score), font = (font.Font(size=16)), fg = "green")
game_score.pack()

display_words = Label(root , font = (font.Font(size=28)), pady = 10)
display_words.pack()

time_left = Label(root, text = "Game Ends in : -", font = (font.Font(size=14)), fg = "orange")
time_left.pack()



b1 = Button(root,text="START",font=("arial",30,"bold"), fg = "black", bg = "pink", bd = 0,command = startGame)
b2 = Button(root,text="RESET",font=("arial",30,"bold"),  fg = "black", bg = "light blue", bd = 0,command = resetGame)
b3 = Button(root,text="EXIT",font=("arial",30,"bold"),  fg = "black", bg = "red", bd = 0,command = exit)
e1 = Entry(root,width=15)
b1.place(x=100,y=250)
b2.place(x=250,y=250)
b3.place(x=400,y=250)
e1.place(x=240,y=150)
time_left.place(x=240,y=130)



root.mainloop()