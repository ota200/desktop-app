from tkinter import *

root = Tk()

def app():
	button = Button(root, text="Click Me")
	button.pack()

def label():
	label_1 = Label(root, text="hi")
	label_2 = Label(root, text="hi ota")

	label_1.pack()
	label_2.pack()

app()
label()
app()
label()


root.mainloop()