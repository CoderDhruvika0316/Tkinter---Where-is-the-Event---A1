from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("300x300+625+200")

def handle_keys(event):
    print(event.char)

window.bind("<Key>", handle_keys)

def handle_button(event):
    print("My precious button was clicked!")

button = Button(text = "Click me! I look beautiful!")
button.pack()
window.bind("<Button-1>", handle_button)

window.mainloop()