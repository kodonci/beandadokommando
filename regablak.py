# Regisztrációs ablak és importálás

from tkinter import *
import osztaly

p = osztaly.Cegadatok()


class regAblak:

    def futtat(self):
        self.regisztracioAblak = Tk()
        self.regisztracioAblak.configure(bg='green')
        self.regisztracioAblak.title('Regisztráció')
        self.regisztracioAblak.minsize(240, 200)

        self.cegnevregLabel = Label(self.regisztracioAblak, text='Cégnév: ', fg='yellow', bg='green')
        self.cegnevregLabel.grid(row=0, column=0, padx=2, pady=2)

        self.jelszoregLabel = Label(self.regisztracioAblak, text='Jelszó: ', fg='yellow', bg='green')
        self.jelszoregLabel.grid(row=1, column=0, padx=2, pady=2)

        self.szekhelyLabel = Label(self.regisztracioAblak, text='Székhely: ', fg='yellow', bg='green')
        self.szekhelyLabel.grid(row=2, column=0, padx=2, pady=2)

        self.tulajnevLabel = Label(self.regisztracioAblak, text='Tulajdonos neve: ', fg='yellow', bg='green')
        self.tulajnevLabel.grid(row=3, column=0, padx=2, pady=2)

        self.alapitasLabel = Label(self.regisztracioAblak, text='Alapítás éve: ', fg='yellow', bg='green')
        self.alapitasLabel.grid(row=4, column=0, padx=2, pady=2)

        self.adoszamLabel = Label(self.regisztracioAblak, text='Adószám: ', fg='yellow', bg='green')
        self.adoszamLabel.grid(row=5, column=0, padx=2, pady=2)

        self.cegnevregEntry = Entry(self.regisztracioAblak, width=28)
        self.cegnevregEntry.grid(row=0, column=1, padx=2, pady=2)

        self.jelszoregEntry = Entry(self.regisztracioAblak, width=28, show='*')
        self.jelszoregEntry.grid(row=1, column=1, padx=2, pady=2)

        self.szekhelyEntry = Entry(self.regisztracioAblak, width=28)
        self.szekhelyEntry.grid(row=2, column=1, padx=2, pady=2)

        self.tulajnevEntry = Entry(self.regisztracioAblak, width=28)
        self.tulajnevEntry.grid(row=3, column=1, padx=2, pady=2)

        self.alapitasEntry = Entry(self.regisztracioAblak, width=28)
        self.alapitasEntry.grid(row=4, column=1, padx=2, pady=2)

        self.adoszamEntry = Entry(self.regisztracioAblak, width=28)
        self.adoszamEntry.grid(row=5, column=1, padx=2, pady=2)

        self.regisztracio2_gomb = Button(self.regisztracioAblak, text='Regisztráció', command=self.export)
        self.regisztracio2_gomb.place(x=100, y=160)

        self.regisztracioAblak.mainloop()

    def export(self):
        p.adoszam = self.adoszamEntry.get()
        p.alapitaseve = self.alapitasEntry.get()
        p.tulajnev = self.tulajnevEntry.get()
        p.szekhely = self.szekhelyEntry.get()
        p.jelszo = self.jelszoregEntry.get()
        p.cegnev = self.cegnevregEntry.get()
        p.kiiras()

        sikeres = Tk()
        sikeres.configure(bg='green')
        sikeres.title('Siker!')
        sikeres.minsize(350, 80)

        sikeresLabel = Label(sikeres, text='Sikeres regisztrálás!'
                                           '\n Az OK gomb lenyomása után bezárhatja a regisztrációs ablakot!'
                             , bg='green', fg='yellow')
        sikeresLabel.grid(row=0, column=0, pady=5, padx=5)

        okgomb = Button(sikeres, text='OK', command=sikeres.destroy)
        okgomb.grid(row=1, column=0, pady=5, padx=5)

        sikeres.mainloop()
