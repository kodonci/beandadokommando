# A regisztrációhoz szükséges Class és az adatok importálását végző függvény

class Cegadatok:
    cegnev = ''
    jelszo = ''
    szekhely = ''
    tulajnev = ''
    alapitaseve = ''
    adoszam = ''

    def __init__(self):
        self.cegnev = 'Hiba'
        self.jelszo = 'Hiba'
        self.szekhely = 'Hiba'
        self.tulajnev = 'Hiba'
        self.alapitaseve = 'Hiba'
        self.adoszam = 'Hiba'

    def kiiras(self):
        cegnev = self.cegnev
        with open('adatok.txt', 'a', encoding='utf-8') as ceg:
            ceg.write('\n' + cegnev)

        jelszo = self.jelszo
        with open('adatok.txt', "a", encoding='utf-8') as jelszoadat:
            jelszoadat.write(';' + jelszo)

        szekhely = self.szekhely
        tulajnev = self.tulajnev
        alapitaseve = self.alapitaseve
        adoszam = self.adoszam
        with open('ceginfo.txt', "a", encoding='utf-8') as ceginformacio:
            ceginformacio.write('\nCégnév: ' + cegnev + ', Székhely:  ' + szekhely +
                                ', Tulajdonos neve: ' + tulajnev + ', Alapítás éve: ' + alapitaseve +
                                ', Adószám: ' + adoszam)