from tkinter import *

window = Tk()
window.title('Calculator')
window.resizable(False, False)

ingresso = Entry(window, width=50, borderwidth=3)
ingresso.grid(row=0, column=0, columnspan=4, pady=5)


#Funzione

def premi_bottone(number):

    current = ingresso.get()
    ingresso.delete(0, END)
    ingresso.insert(0, str(current) + str(number))

def cancella():
    ingresso.delete(0, END)

def addizione():
    primo_numero = ingresso.get()
    global primo_num
    global math
    math = 'addition'
    primo_num = int(primo_numero)
    ingresso.delete(0, END)

def sottrazione():
    primo_numero = ingresso.get()
    global primo_num
    global math
    math = 'subtraction'
    primo_num = int(primo_numero)
    ingresso.delete(0, END)
def moltiplicazione():
    primo_numero = ingresso.get()
    global primo_num
    global math
    math = 'multiplication'
    primo_num = int(primo_numero)
    ingresso.delete(0, END)
def divisione():
    primo_numero = ingresso.get()
    global primo_num
    global math
    math = 'division'
    primo_num = int(primo_numero)
    ingresso.delete(0, END)
def risultato():

    secondo_numero = ingresso.get()
    ingresso.delete(0, END)
    if math == 'addiction':
        ingresso.insert(0, primo_num + int(secondo_numero))
    if math == 'subtraction':
        ingresso.insert(0, primo_num - int(secondo_numero))
    if math == 'multiplication':
            ingresso.insert(0, primo_num * int(secondo_numero))
    if math == 'division':
        ingresso.insert(0, primo_num / int(secondo_numero))


#Bottoni
bottone1 = Button(window, text='1', padx=40, pady= 20, command=lambda: premi_bottone(1))
bottone2 = Button(window, text='2', padx=40, pady= 20, command=lambda: premi_bottone(2))
bottone3 = Button(window, text='3', padx=40, pady= 20, command=lambda: premi_bottone(3))
bottone4 = Button(window, text='4', padx=40, pady= 20, command=lambda: premi_bottone(4))
bottone5 = Button(window, text='5', padx=40, pady= 20, command=lambda: premi_bottone(5))
bottone6 = Button(window, text='6', padx=40, pady= 20, command=lambda: premi_bottone(6))
bottone7 = Button(window, text='7', padx=40, pady= 20, command=lambda: premi_bottone(7))
bottone8 = Button(window, text='8', padx=40, pady= 20, command=lambda: premi_bottone(8))
bottone9 = Button(window, text='9', padx=40, pady= 20, command=lambda: premi_bottone(9))
bottone0 = Button(window, text='0', padx=40, pady= 20, command=lambda: premi_bottone(0))
bottone_addizione = Button(window, text='+', padx=39, pady= 20, command=addizione)
bottone_sottrazione = Button(window, text='-', padx=39, pady= 20, command=sottrazione)
bottone_moltiplicazione = Button(window, text='x', padx=39, pady= 20, command=moltiplicazione)
bottone_divisione = Button(window, text='/', padx=39, pady= 20, command=divisione)
bottone_uguale = Button(window, text='=', padx=39, pady= 20, command=risultato)
bottone_reset = Button(window, text='C', padx=39, pady= 20, command=cancella)

#Display buttons

bottone1.grid(row=3, column=1)
bottone2.grid(row=3, column=2)
bottone3.grid(row=3, column=3)

bottone4.grid(row=2, column=1)
bottone5.grid(row=2, column=2)
bottone6.grid(row=2, column=3)

bottone7.grid(row=1, column=1)
bottone8.grid(row=1, column=2)
bottone9.grid(row=1, column=3)

bottone0.grid(row=4, column=2)

bottone_addizione.grid(row=1, column=4)
bottone_sottrazione.grid(row=2, column=4)
bottone_moltiplicazione.grid(row=3, column=4)
bottone_divisione.grid(row=4, column=4)

bottone_uguale.grid(row=4, column=3)
bottone_reset.grid(row=4, column=1)

if __name__ == '__main__':
    window.mainloop()

