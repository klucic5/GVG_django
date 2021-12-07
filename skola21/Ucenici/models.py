from sqlite3 import *
baza = 'db.sqlite3'
class Ucenik:
    def __init__(self, ID=None, ime='', prezime='', datumRodenja=''):
        self.ID = ID
        self.I = ime
        self.P = prezime
        self.D = datumRodenja
    def __repr__(self):
        return f'{self.I} {self.P}'
    def __eq__(self, u):
        return self.ID == u.ID
    def __lt__(self, u):
        return self.P < u.P
    def pohrani(self):
        conn = connect(baza)
        curr = conn.cursor()
        if self.ID != None:
            upit = f'''UPDATE Ucenik
                SET ime="{self.I}",
                prezime="{self.P}",
                datumRodenja="{self.D}"
                WHERE ID={self.ID}'''
        else:
            upit = f'''INSERT INTO Ucenik (Ime, Prezime, DatumRodenja)
                VALUES ("{self.I}", "{self.P}", "{self.D}")'''
        curr.execute(upit)
        if self.ID == None:
            self.ID = curr.lastrowid
        conn.commit()
        conn.close()
    def obrisi(self):
        conn = connect(baza)
        curr = conn.cursor()
        upit = f'DELETE FROM Ucenik WHERE ID={self.ID}'
        curr.execute(upit)
        conn.commit()
        conn.close()
    #dohvaća sve učenike iz tablice Ucenici
    def dohvati_sve():
        conn = connect(baza)
        curr = conn.cursor()
        upit = f'''SELECT ID, Ime, Prezime, DatumRodenja
            FROM Ucenik ORDER BY Prezime ASC'''
        data = []
        for t in curr.execute(upit):
            data.append(Ucenik(t[0], t[1], t[2], t[3]))
        conn.close()
        return data

