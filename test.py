import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GCheckBox_381=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_381["font"] = ft
        GCheckBox_381["fg"] = "#333333"
        GCheckBox_381["justify"] = "center"
        GCheckBox_381["text"] = "  Titre"
        GCheckBox_381.place(x=90,y=80,width=70,height=25)
        GCheckBox_381["offvalue"] = "0"
        GCheckBox_381["onvalue"] = "1"
        GCheckBox_381["command"] = self.GCheckBox_381_command

        GCheckBox_396=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_396["font"] = ft
        GCheckBox_396["fg"] = "#333333"
        GCheckBox_396["justify"] = "center"
        GCheckBox_396["text"] = "Clef"
        GCheckBox_396.place(x=250,y=80,width=70,height=25)
        GCheckBox_396["offvalue"] = "0"
        GCheckBox_396["onvalue"] = "1"
        GCheckBox_396["command"] = self.GCheckBox_396_command

        GCheckBox_779=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_779["font"] = ft
        GCheckBox_779["fg"] = "#333333"
        GCheckBox_779["justify"] = "center"
        GCheckBox_779["text"] = "Note"
        GCheckBox_779.place(x=450,y=80,width=70,height=25)
        GCheckBox_779["offvalue"] = "0"
        GCheckBox_779["onvalue"] = "1"
        GCheckBox_779["command"] = self.GCheckBox_779_command

        GCheckBox_296=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_296["font"] = ft
        GCheckBox_296["fg"] = "#333333"
        GCheckBox_296["justify"] = "center"
        GCheckBox_296["text"] = "Genre"
        GCheckBox_296.place(x=90,y=130,width=70,height=25)
        GCheckBox_296["offvalue"] = "0"
        GCheckBox_296["onvalue"] = "1"
        GCheckBox_296["command"] = self.GCheckBox_296_command

        GCheckBox_523=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_523["font"] = ft
        GCheckBox_523["fg"] = "#333333"
        GCheckBox_523["justify"] = "center"
        GCheckBox_523["text"] = "Opus"
        GCheckBox_523.place(x=450,y=130,width=70,height=25)
        GCheckBox_523["offvalue"] = "0"
        GCheckBox_523["onvalue"] = "1"
        GCheckBox_523["command"] = self.GCheckBox_523_command

        GCheckBox_969=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_969["font"] = ft
        GCheckBox_969["fg"] = "#333333"
        GCheckBox_969["justify"] = "center"
        GCheckBox_969["text"] = "Composeur"
        GCheckBox_969.place(x=240,y=130,width=130,height=30)
        GCheckBox_969["offvalue"] = "0"
        GCheckBox_969["onvalue"] = "1"
        GCheckBox_969["command"] = self.GCheckBox_969_command

        GLabel_124=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_124["font"] = ft
        GLabel_124["fg"] = "#333333"
        GLabel_124["justify"] = "center"
        GLabel_124["text"] = "Quelles propriétées voulez-vous utiliser ? "
        GLabel_124.place(x=0,y=40,width=600,height=25)

        GLabel_551=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_551["font"] = ft
        GLabel_551["fg"] = "#333333"
        GLabel_551["justify"] = "center"
        GLabel_551["text"] = "Quelles méthodes de mesure voulez-vous choisir ? "
        GLabel_551.place(x=0,y=190,width=600,height=25)

        GCheckBox_136=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_136["font"] = ft
        GCheckBox_136["fg"] = "#333333"
        GCheckBox_136["justify"] = "center"
        GCheckBox_136["text"] = "Jaro"
        GCheckBox_136.place(x=80,y=280,width=70,height=25)
        GCheckBox_136["offvalue"] = "0"
        GCheckBox_136["onvalue"] = "1"
        GCheckBox_136["command"] = self.GCheckBox_136_command

        GCheckBox_691=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_691["font"] = ft
        GCheckBox_691["fg"] = "#333333"
        GCheckBox_691["justify"] = "center"
        GCheckBox_691["text"] = "Jaccar"
        GCheckBox_691.place(x=270,y=280,width=70,height=25)
        GCheckBox_691["offvalue"] = "0"
        GCheckBox_691["onvalue"] = "1"
        GCheckBox_691["command"] = self.GCheckBox_691_command

        GCheckBox_453=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_453["font"] = ft
        GCheckBox_453["fg"] = "#333333"
        GCheckBox_453["justify"] = "center"
        GCheckBox_453["text"] = "monge elkan"
        GCheckBox_453.place(x=450,y=280,width=100,height=25)
        GCheckBox_453["offvalue"] = "0"
        GCheckBox_453["onvalue"] = "1"
        GCheckBox_453["command"] = self.GCheckBox_453_command

        GCheckBox_548=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_548["font"] = ft
        GCheckBox_548["fg"] = "#333333"
        GCheckBox_548["justify"] = "center"
        GCheckBox_548["text"] = "Identity"
        GCheckBox_548.place(x=90,y=340,width=70,height=25)
        GCheckBox_548["offvalue"] = "0"
        GCheckBox_548["onvalue"] = "1"
        GCheckBox_548["command"] = self.GCheckBox_548_command

        GCheckBox_504=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_504["font"] = ft
        GCheckBox_504["fg"] = "#333333"
        GCheckBox_504["justify"] = "center"
        GCheckBox_504["justify"] = "center"
        GCheckBox_504["text"] = "Ngram"
        GCheckBox_504.place(x=270,y=340,width=70,height=25)
        GCheckBox_504["offvalue"] = "0"
        GCheckBox_504["onvalue"] = "1"
        GCheckBox_504["command"] = self.GCheckBox_504_command




        GLineEdit_625=tk.Entry(root)
        GLineEdit_625["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_625["font"] = ft
        GLineEdit_625["fg"] = "#333333"
        GLineEdit_625["justify"] = "center"
        GLineEdit_625.place(x=80,y=310,width=70,height=25)

        GLineEdit_304=tk.Entry(root)
        GLineEdit_304["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_304["font"] = ft
        GLineEdit_304["fg"] = "#333333"
        GLineEdit_304["justify"] = "center"
        GLineEdit_304.place(x=270,y=310,width=70,height=25)

        GLineEdit_353=tk.Entry(root)
        GLineEdit_353["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_353["font"] = ft
        GLineEdit_353["fg"] = "#333333"
        GLineEdit_353["justify"] = "center"
        GLineEdit_353.place(x=450,y=310,width=70,height=25)

        GLineEdit_331=tk.Entry(root)
        GLineEdit_331["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_331["font"] = ft
        GLineEdit_331["fg"] = "#333333"
        GLineEdit_331["justify"] = "center"
        GLineEdit_331.place(x=80,y=370,width=70,height=25)

        GLineEdit_375=tk.Entry(root)
        GLineEdit_375["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_375["font"] = ft
        GLineEdit_375["fg"] = "#333333"
        GLineEdit_375["justify"] = "center"
        GLineEdit_375.place(x=230,y=370,width=70,height=25)

        GLineEdit_719=tk.Entry(root)
        GLineEdit_719["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_719["font"] = ft
        GLineEdit_719["fg"] = "#333333"
        GLineEdit_719["justify"] = "center"
        GLineEdit_719.place(x=450,y=370,width=70,height=25)
        GLineEdit_719.configure(state='disable')


        GLineEdit_705=tk.Entry(root)
        GLineEdit_705["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_705["font"] = ft
        GLineEdit_705["fg"] = "#333333"
        GLineEdit_705["justify"] = "center"
        GLineEdit_705.place(x=310,y=370,width=70,height=25)

        GCheckBox_555 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_555["font"] = ft
        GCheckBox_555["fg"] = "#333333"
        GCheckBox_555["justify"] = "center"
        GCheckBox_555["text"] = "levenshtein"
        GCheckBox_555.place(x=450, y=340, width=90, height=25)
        GCheckBox_555["offvalue"] = "0"
        GCheckBox_555["onvalue"] = "1"
        GCheckBox_555["command"] = GLineEdit_719.configure(state='normal')
    def GCheckBox_381_command(self):
        print("command")


    def GCheckBox_396_command(self):
        print("command")


    def GCheckBox_779_command(self):
        print("command")


    def GCheckBox_296_command(self):
        print("command")


    def GCheckBox_523_command(self):
        print("command")


    def GCheckBox_969_command(self):
        print("command")


    def GCheckBox_136_command(self):
        print("command")


    def GCheckBox_691_command(self):
        print("command")


    def GCheckBox_453_command(self):
        print("command")


    def GCheckBox_548_command(self):
        print("command")


    def GCheckBox_504_command(self):
        print("command")




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
