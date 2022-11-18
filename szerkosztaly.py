# A Word fájlhoz szükséges Class és az adatok importálását végző függvény

import aspose.words as aw


class Exportadatok:
    cim = ''
    kinek = ''
    mirol = ''
    tetel1 = ''
    tetel2 = ''
    tetel3 = ''
    tetel4 = ''
    tetel5 = ''
    tetel6 = ''

    def __init__(self):
        self.cim = 'Hiba'
        self.kinek = 'Hiba'
        self.mirol = 'Hiba'
        self.tetel1 = 'Hiba'
        self.tetel2 = 'Hiba'
        self.tetel3 = 'Hiba'
        self.tetel4 = 'Hiba'
        self.tetel5 = 'Hiba'
        self.tetel6 = 'Hiba'

    def word(self):
        dokumentum = aw.Document()
        builder = aw.DocumentBuilder(dokumentum)
        tablazat = builder.start_table()
        builder.insert_cell()
        tablazat.auto_fit(aw.tables.AutoFitBehavior.AUTO_FIT_TO_CONTENTS)

        builder.cell_format.vertical_alignment = aw.tables.CellVerticalAlignment.CENTER
        builder.write('Árajánlat')
        builder.end_row()

        builder.insert_cell()
        builder.write('Cím: ')
        builder.insert_cell()
        builder.write(self.cim)
        builder.end_row()

        builder.insert_cell()
        builder.write('Kinek a részére: ')
        builder.insert_cell()
        builder.write(self.kinek)
        builder.end_row()

        builder.insert_cell()
        builder.write('Téma: ')
        builder.insert_cell()
        builder.write(self.mirol)
        builder.end_row()

        builder.insert_cell()
        builder.write('Tétel(ek): ')
        builder.insert_cell()
        builder.writeln(self.tetel1)
        builder.writeln(self.tetel2)
        builder.writeln(self.tetel3)
        builder.writeln(self.tetel4)
        builder.writeln(self.tetel5)
        builder.writeln(self.tetel6)
        builder.end_row()

        builder.end_table()

        dokumentum.save("arajanlat.docx")