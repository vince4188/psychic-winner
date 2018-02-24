from sys import exit
from tkinter import *
from tkinter.colorchooser import *

color = "black"

def connect(event=None):
	if username.get().strip():
		signIn.destroy()
        
def close():
	exit(0)

def send(event=None):
        if message.get().strip():
                listBox.insert(END, "%s: %s" % (username.get(), message.get()))
                listBox.itemconfig(END, {'fg': color})
                listBox.see(END)
                message.set("")

def changeColor(even=None):
	global color
	color = askcolor()
	color = color[1]
	colorButton.config(bg = color)
	messageEntry.config(foreground = color)
	userLabel.config(foreground = color)

	
if __name__ == "__main__":
	signIn = Tk()
	signIn.title("RWC Login")
	signIn.protocol("WM_DELETE_WINDOW", close)
	
	userLabel = Label(signIn, text = "Enter your username:   ")
	userLabel.grid(row=0, column=0)

	username = StringVar()
	userEntry = Entry(signIn, textvariable=username)
	userEntry.grid(row=0, column=1)
	
	userEntry.bind("<Return>", connect)
	
	enterButton = Button(signIn, text="Sign In", command=connect)
	enterButton.grid(row=0, column=2)
	
	signIn.mainloop()

        #chat box
	chatBox = Tk()
	chatBox.title("RWC Chat")
	chatBox.protocol("WM_DELETE_WINDOW", close)

	message = StringVar()
        #top frame
	topFrame = Frame(chatBox)
	topFrame.pack(fill=BOTH, expand=True)
	scrollBar = Scrollbar(topFrame, orient=VERTICAL)
	scrollBar.pack(side=RIGHT, fill=Y)
	listBox = Listbox(topFrame, yscrollcommand=scrollBar.set)
	listBox.pack(side=LEFT, expand=True, fill=BOTH)
	scrollBar.config(command=listBox.yview)
        #bot frame
	botFrame = Frame(chatBox, height = 1)
	botFrame.pack(fill=X)
	userLabel = Label(botFrame, text = "%s: " % username.get(), foreground=color)
	userLabel.pack(side=LEFT)
	
	messageEntry = Entry(botFrame, textvariable=message, foreground=color)
	messageEntry.bind("<Return>", send)

	sendButton = Button(botFrame, text="Send", command=send)
	sendButton.pack(side=RIGHT)

	colorButton = Button(botFrame, text=" ", command=changeColor, bg=color)
	colorButton.pack(side=RIGHT)
	messageEntry.pack(expand=True, fill=BOTH)

	chatBox.mainloop()
