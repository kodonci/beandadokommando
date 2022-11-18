# Árajnálat készítő program - terv:
# 1. beléptetés (regisztrálás, nem regisztrált cég/jelszóhiba esetén új ablakban hiba)
# 2. árajánlatkészítő felület (ha mező üresen marad, hibaablak) (gombok, beviteli mezők, szövegek)
# 3. elkészült ajánlat exportálása Word-be (táblázatba)

from tkinter import *

import regablak
import szerkeszto
import os

regAblak = regablak.regAblak()
szerkAblak = szerkeszto.szerkesztoAblak()

# Belépépsi adatokat vizsgáló függvény
def belepes():
    userdata = []
    if os.path.exists('adatok.txt'):
        with open('adatok.txt', 'r', encoding='utf-8') as adat:
            for sor in adat:
                userdata.append(sor.strip().split(';'))

    user = str(cegnevEntry.get())
    felhasznalo_van = False
    i = 0
    for i in range(len(userdata)):
        if userdata[i][0] == user:
            felhasznalo_van = True
            break
    if felhasznalo_van:
        jelszo = str(jelszoEntry.get())
        while jelszo != userdata[i][1]:
            hibaablak = Toplevel(bejelentkezes)
            hibaablak.configure(bg='red')
            hibaablak.title('Hiba!')
            hibaablak.geometry('200x80')
            uzenet = Label(hibaablak, text='Hibás jelszó!', fg='white', bg='red')
            uzenet.place(x=65, y=10)
            ok = Button(hibaablak, text='OK', command=hibaablak.destroy)
            ok.place(x=85, y=40)
            cegnevEntry.delete(0, END)
            jelszoEntry.delete(0, END)
            hibaablak.mainloop()
        else:
            bejelentkezes.destroy()
            szerkAblak.futtatszerkeszto()
    else:
        hibaablak = Toplevel(bejelentkezes)
        hibaablak.configure(bg='red')
        hibaablak.title('Hiba!')
        hibaablak.geometry('200x80')
        uzenet = Label(hibaablak, text='Nincs ilyen cégnév!', fg='white', bg='red')
        uzenet.place(x=50, y=10)
        ok = Button(hibaablak, text='OK', command=hibaablak.destroy)
        ok.place(x=90, y=40)
        cegnevEntry.delete(0, END)
        jelszoEntry.delete(0, END)
        hibaablak.mainloop()


# Bejelentkezés ablak kódja
bejelentkezes = Tk()
bejelentkezes.configure(bg='green')
bejelentkezes.title('Bejelentkezés')
bejelentkezes.minsize(240, 100)

cegnevLabel = Label(bejelentkezes, text='Cégnév: ', fg='yellow', bg='green')
cegnevLabel.grid(row=0, column=0, padx=2, pady=2)

jelszoLabel = Label(bejelentkezes, text='Jelszó: ', fg='yellow', bg='green')
jelszoLabel.grid(row=1, column=0, padx=2, pady=2)

cegnevEntry = Entry(bejelentkezes, width=28)
cegnevEntry.grid(row=0, column=1, padx=2, pady=2)

jelszoEntry = Entry(bejelentkezes, width=28, show='*')
jelszoEntry.grid(row=1, column=1, padx=2, pady=2)

regisztracio_gomb = Button(bejelentkezes, text='Regisztráció', command=regAblak.futtat)
regisztracio_gomb.place(x=150, y=60)

belepes_gomb = Button(bejelentkezes, text='Belépés', command=belepes)
belepes_gomb.place(x=60, y=60)

bejelentkezes.mainloop()