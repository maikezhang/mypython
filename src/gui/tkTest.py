from tkinter import *

class myApplication(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel=Label(self,text='maikezhang  nihao ')
        self.helloLabel.pack()
        self.quitButton=Button(self,text='Quit',command=self.tuichu)
        self.quitButton.pack()

    def tuichu(self):
        print("窗口退出")
        self.quit()


app=myApplication()

app.master.title("123")

app.mainloop()
