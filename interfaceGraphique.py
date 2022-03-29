from tkinter import *
from tkinter.ttk import *

window = Tk()


window.title("Outil RDF")
window.geometry('720x480')

lbl=Label(window, text="OUTIL RDF", font=("Helvetica", 16))
lbl.grid(column=2, row=0)

l0 = Label(window, text='     \n   ',font=("Helvetica",7))
l0.grid(column=2, row=1)


lbl1=Label(window, text="Quelles propriétées choisissez-vous ?", font=("Helvetica", 10))
lbl1.grid(column=2,row=2,columnspan=3)

l0 = Label(window, text='     \n   ')
l0.grid(column=2, row=3)

chk_state1 = BooleanVar()
chk_state2 = BooleanVar()
chk_state3 = BooleanVar()
chk_state4 = BooleanVar()
chk_state5 = BooleanVar()
chk_state6 = BooleanVar()

chk_state1.set(True)
chk_state2.set(True)
chk_state3.set(True)
chk_state4.set(True)
chk_state5.set(True)
chk_state6.set(True)



rad1 = Checkbutton(window, text='Titre', var=chk_state1)
rad2 = Checkbutton(window, text='Note', var=chk_state2)
rad3 = Checkbutton(window, text='Composeur', var=chk_state3)
rad4 = Checkbutton(window, text='Genre', var=chk_state4)
rad5 = Checkbutton(window, text='Clef', var=chk_state5)
rad6 = Checkbutton(window, text='Opus', var=chk_state6)



rad1.grid(row=3, column=0)
rad2.grid(column=1, row=3)
rad3.grid(column=2, row=3)
rad4.grid(column=3, row=3)
rad5.grid(column=4, row=3)
rad6.grid(column=5, row=3)

l1 = Label(window, text='     \n   ',font=("Helvetica", 20))
l1.grid(column=2, row=4)

lbl=Label(window, text="Quelles méthodes de comparaison voulez-vous choisir ?", font=("Helvetica", 10))
lbl.grid(column=2, row=4)

l2 = Label(window, text='     \n   ')
l2.grid(column=2, row=5)


window.mainloop()