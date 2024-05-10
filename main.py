from abc import ABC, abstractmethod


class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        foglalas_statusz = False

    @abstractmethod
    def foglalas_rogzitese(self):
        pass

    @abstractmethod
    def foglalas_torlese(self):
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)

    def foglalas_rogzitese(self):
        if self.foglalt:
            self.foglalt = True
        else:
            print('Ez a szoba mar foglalt.')

    def foglalas_torlese(self):
        if self.foglalt:
            self.foglalt = False
        else:
            print('Ez a szoba szabad.')


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)

    def foglalas_rogzitese(self):
        if self.foglalt:
            self.foglalt = True
        else:
            print('Ez a szoba mar foglalt.')

    def foglalas_torlese(self):
        if self.foglalt:
            self.foglalt = False
        else:
            print('Ez a szoba szabad.')


class Szalloda:
    def __init__(self):
        self.szobak = []

    def szobak_hozzaadasa(self, szobak):
        szabad_szobak = []
        for szoba in self.szobak:
            if not szobak.foglalas_rogzitese():
                szabad_szobak.append(szobak.szobaszam)
        return szabad_szobak

    def szabad_szobak(self):
        szabad_szobak = []
        for szoba in self.szobak:
            if not szoba.foglalt:
                szabad_szobak.append(szoba.szobaszam)
        return szabad_szobak


class Foglalas:
    def __init__(self):
        self.Szalloda = Szalloda()

    def szoba_adatok(self):
        self.Szalloda.szobak_hozzaadasa(EgyagyasSzoba('23', '1500'))
        self.Szalloda.szobak_hozzaadasa(KetagyasSzoba('36', '1750'))

    def felhasznaloi_adatbevitel(self):
        while True:
            print('1. Szabad szobak listazasa')
            print('2. Kilepes')

            kivalasztott_opcio = input('Valasszon a fenti opciok kozul: ')

            if kivalasztott_opcio == '1':
                print('Szabad szobak:', self.Szalloda.szabad_szobak())
            else:
                break


foglalas = Foglalas()
foglalas.szoba_adatok()
foglalas.felhasznaloi_adatbevitel()

