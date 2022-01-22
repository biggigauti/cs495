import tkinter as tk
import random
from tkinter import messagebox

wn = tk.Tk()
wn.geometry('600x600') #sets window dimensions
wn.title("Python GUI Program") #adds title to tkinter window (top)
wn.config(background = "grey") #sets background color

moleNumber = random.randint(0, 8) #Initialize moleNumber
counter = 0 #Initialize counter

def onClick():
    global counter #keeps track of how many times you have miseed
    global myScore #label
    global moleNumber #random number between 0-8
    myScore['text'] = counter #update score label
    moleNumber = random.randint(0, 8)
    if (moleNumber == 1):
        messagebox.showinfo(message = f'You Suck! You missed {counter} times!') #displays very friendly message when you lose
        counter = 0 #restart counter when you lose
        myScore['text'] = 0
    counter += 1

myLabel = tk.Label(wn, text = "Miss Counter:", background = "grey") #tk.Label makes label
myLabel.grid(row=0, column=0) #puts label/object in the right place
myScore = tk.Label(wn, text = counter, background = "grey")
myScore.grid(row=0, column=1)

btn1 = tk.Button(wn, text = "0", command = onClick) #tk.Button makes a button
btn1.grid(row = 2, column = 1)
btn2 = tk.Button(wn, text = "1", command = onClick)
btn2.grid(row = 2, column = 2)
btn3 = tk.Button(wn, text = "2", command = onClick)
btn3.grid(row = 2, column = 3)
btn4 = tk.Button(wn, text = "3", command = onClick)
btn4.grid(row = 3, column = 1)
btn5 = tk.Button(wn, text = "4", command = onClick)
btn5.grid(row = 3, column = 2)
btn6 = tk.Button(wn, text = "5", command = onClick)
btn6.grid(row = 3, column = 3)
btn7 = tk.Button(wn, text = "6", command = onClick)
btn7.grid(row = 4, column = 1)
btn8 = tk.Button(wn, text = "7", command = onClick)
btn8.grid(row = 4, column = 2)
btn9 = tk.Button(wn, text = "8", command = onClick)
btn9.grid(row = 4, column = 3)

wn.mainloop() #run game

# https://www.tutorialspoint.com/python/tk_button.htm
#I didn't exactly remember the ins and outs of tkinter but the discussion in class helped alot. I didn't use the class help documents, only simple stuff from memory.
#I used the link above to read about the different attributes that the buttons or labels had.
#I would say I wrote 100% of the code since I didn't look at other code sources for help. However, I used the help document a lot. But that's just for general syntax which i pieced together myself.

#if __name__ == '__main__':