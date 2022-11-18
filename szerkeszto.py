# Az árajnálatkészítő ablak kódja és importálás

from tkinter import *
import szerkosztaly

s = szerkosztaly.Exportadatok()


class szerkesztoAblak:

    def futtatszerkeszto(self):
        self.szerkeszto = Tk()
        self.szerkeszto.title('Árajnálat készítő (fejlesztés alatt)')
        self.szerkeszto.configure(bg='green')
        self.szerkeszto.minsize(600, 300)

        self.arajanlatLabel = Label(self.szerkeszto, text='Az árajánlat...', fg='yellow', bg='green')
        self.arajanlatLabel.grid(row=0, column=1, padx=5, pady=5)

        self.kitoltesLabel = Label(self.szerkeszto, text='Minden mező kitöltése kötelező!'
                                                         '\nNem használt tétel dobozba X-et tegyen!', fg='yellow',
                                   bg='green')
        self.kitoltesLabel.grid(row=0, column=2, padx=5, pady=5)

        self.cimLabel = Label(self.szerkeszto, text='Címe', fg='yellow', bg='green')
        self.cimLabel.grid(row=1, column=1, padx=5, pady=5)
        self.cimEntry = Entry(self.szerkeszto, width=53)
        self.cimEntry.grid(row=1, column=2, padx=2, pady=2)

        self.kinekLabel = Label(self.szerkeszto, text='Kinek a részére', fg='yellow', bg='green')
        self.kinekLabel.grid(row=2, column=1, padx=5, pady=5)
        self.kinekEntry = Entry(self.szerkeszto, width=53)
        self.kinekEntry.grid(row=2, column=2, padx=2, pady=2)

        self.mirolLabel = Label(self.szerkeszto, text='Témája', fg='yellow', bg='green')
        self.mirolLabel.grid(row=3, column=1, padx=5, pady=5)
        self.mirolEntry = Entry(self.szerkeszto, width=53)
        self.mirolEntry.grid(row=3, column=2, padx=2, pady=2)

        self.tetelLabel = Label(self.szerkeszto, text='Tételei (max. 6)', fg='yellow', bg='green')
        self.tetelLabel.grid(row=4, column=1, padx=5, pady=5)
        self.tetel1Entry = Entry(self.szerkeszto, width=53)
        self.tetel1Entry.grid(row=4, column=2, padx=5, pady=5)
        self.tetel2Entry = Entry(self.szerkeszto, width=53)
        self.tetel2Entry.grid(row=5, column=2, padx=5, pady=5)
        self.tetel3Entry = Entry(self.szerkeszto, width=53)
        self.tetel3Entry.grid(row=6, column=2, padx=5, pady=5)
        self.tetel4Entry = Entry(self.szerkeszto, width=53)
        self.tetel4Entry.grid(row=7, column=2, padx=5, pady=5)
        self.tetel5Entry = Entry(self.szerkeszto, width=53)
        self.tetel5Entry.grid(row=8, column=2, padx=5, pady=5)
        self.tetel6Entry = Entry(self.szerkeszto, width=53)
        self.tetel6Entry.grid(row=9, column=2, padx=5, pady=5)

        self.word = Button(self.szerkeszto, text='Exportálás', command=self.wordexport)
        self.word.grid(row=0, column=3, pady=5, padx=5, rowspan=2)

        self.logoLabel = Label()
        self.logoLabel.grid(row=2, column=3, padx=5, pady=5, rowspan=7)
        self.logo = PhotoImage(file='logo.png')
        self.logoLabel['image'] = self.logo

        self.szerkeszto.mainloop()

    def wordexport(self):
        s.cim = self.cimEntry.get()
        s.mirol = self.mirolEntry.get()
        s.kinek = self.kinekEntry.get()
        s.tetel1 = self.tetel1Entry.get()
        s.tetel2 = self.tetel2Entry.get()
        s.tetel3 = self.tetel3Entry.get()
        s.tetel4 = self.tetel4Entry.get()
        s.tetel5 = self.tetel5Entry.get()
        s.tetel6 = self.tetel6Entry.get()
        s.word()

        sikeres = Tk()
        sikeres.configure(bg='green')
        sikeres.title('Siker!')
        sikeres.minsize(350, 80)

        sikeresLabel = Label(sikeres, text='Sikeres exportálás!'
                                           '\n Az OK gomb lenyomása után bezárhatja a szerkesztő ablakot!'
                             , bg='green', fg='yellow')
        sikeresLabel.grid(row=0, column=0, pady=5, padx=5)

        okgomb = Button(sikeres, text='OK', command=sikeres.destroy)
        okgomb.grid(row=1, column=0, pady=5, padx=5)

        sikeres.mainloop()
