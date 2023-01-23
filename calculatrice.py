"""
----
789*
456-
123+
0,/=
----
"""

from tkinter import *
expression = ""


def appuyer(touche):
    if touche == "=":
        calculer()
        return

    global expression
    expression += str(touche)
    equation.set(expression)


def calculer():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)
        expression = total
    except:
        equation.set("erreur")
        expression = ""


def effacer():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="#101419")
    gui.title("Calculatrice")
    gui.geometry("300x385")
    equation = StringVar()
    resultat = Label(gui, bg="#101419", fg="#FFF",
                     textvariable=equation, height="4")
    resultat.grid(columnspan=4)

    boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", ".", 0, "/", "="]
    ligne = 1
    colonne = 0

    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg="grey",
                  fg="#FFF", height=4, width=10)
        b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))

        b.grid(row=ligne, column=colonne)

        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1

    b = Label(gui, text="Effacer", bg="orange",
              fg="#FFF", height=4)
    b.bind("<Button-1>", lambda e: effacer())
    b.grid(columnspan=4, sticky=EW)
    gui.mainloop()
