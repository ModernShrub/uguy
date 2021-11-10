from tkinter import*
import random

root = Tk()
root.geometry("600x400")
root.title("uhysygfeu")
root.configure(bg = "SlateGray3")

wlabel = Label(root, font=("Terminal", 50, "bold"),bg = "SlateGray3")
wlabel.place(relx=0.5, rely=0.45,anchor=CENTER)

slabel = Label(root, bg = "SlateGray3", fg = "snow", font=("Arial", 20, "bold"), text= "Score: 0")
slabel.place(relx=0.1,rely=0.1,anchor=CENTER)

colinp = Entry(root)
colinp.place(relx=0.5,rely=0.65,anchor=CENTER)

class game():
    def __init__(self):
        self._score = 0
        
    def updateg(self):
        self.txt = ["Yellow", "Dark Green", "Blue", "Red", "Cyan", "Snow", "Gold", "Coral", "Maroon", "Tomato"]
        self.rngtxt = random.randint(0, 9)
        self.col = ["yellow", "blue", "tomato", "dark green", "cyan", "red", "gold", "maroon", "coral", "snow"]
        self.rngcol = random.randint(0, 9)
        wlabel['text'] = str(self.txt[self.rngtxt])
        wlabel["fg"] = str(self.col[self.rngcol])
        print(self.txt[self.rngtxt])
        print(self.col[self.rngcol])
        
    def _updates(self, usrinp):
        if usrinp == self.col[self.rngcol]:
            self._score = self._score + random.randint(0, 10)
            slabel['text'] = "Score: " + str(self._score)
            print("user:", usrinp)
        
    def getinp(self,usrinp):
        self._updates(usrinp)
        
        
obj1 = game()
def check():
    inp = colinp.get()
    obj1.getinp(inp)
    colinp.delete(0, END)

btn = Button(root, text="Start", command=obj1.updateg, font=("Arial", 14, "bold"), bg = "steel blue", fg = "snow", relief = FLAT)
btn.place(relx=0.6, rely=0.75,anchor=CENTER)

btn2 = Button(root, text="Check", command=check, font=("Arial", 14, "bold"), bg = "brown4", fg = "snow", relief = FLAT)
btn2.place(relx=0.4, rely=0.75,anchor=CENTER)

root.mainloop()