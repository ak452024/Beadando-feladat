from abc import ABC, abstractmethod


class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalas_statusz = False

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
        if not self.foglalas_statusz:
            self.foglalas_statusz = True
        else:
            print("Ez a szoba foglalt.")

    def foglalas_torlese(self):
        if self.foglalas_statusz:
            self.foglalas_statusz = False
        else:
            print('Ez a szoba szabad.')


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)

    def foglalas_rogzitese(self):
        if not self.foglalas_statusz:
            self.foglalas_statusz = True
        else:
            print("Ez a szoba foglalt.")

    def foglalas_torlese(self):
        if self.foglalas_statusz:
            self.foglalas_statusz = False
        else:
            print('Ez a szoba szabad.')



class Szalloda:
    def __init__(self):
        self._szoba = []

    def szobak_hozzaadasa(self, szoba):
        self._szoba.append(szoba)

    def szabad_szobak_lekerdezese(self):
        szabad_szobak = []

        for szoba in self._szoba:
            if not szoba.foglalas_rogzitese():
                szabad_szobak.append(szoba.szobaszam)
        return szabad_szobak

    def szobafoglalas_szam_szerint(self, szobaszam):
        for szoba in self._szoba:
            if szoba.szobaszam == szobaszam:
                szoba.foglalas_rogzitese()

    def szamszerinti_foglalas_torlese(self, szobaszam):
        for szoba in self._szoba:
            if szoba.szobaszam == szobaszam:
                szoba.foglalas_torlese()

    def ar_lekerdezese(self):
        for szoba in self._szoba:
            return {szoba.szobaszam: szoba.ar}


class Foglalas:
    def __init__(self):
        self.szalloda = Szalloda()

    def szoba_adatok(self):
        self.szalloda.szobak_hozzaadasa(EgyagyasSzoba('17', '1500'))
        self.szalloda.szobak_hozzaadasa(EgyagyasSzoba('18', '1675'))
        self.szalloda.szobak_hozzaadasa(EgyagyasSzoba('19', '1500'))
        self.szalloda.szobak_hozzaadasa(KetagyasSzoba('36', '1995'))
        self.szalloda.szobak_hozzaadasa(KetagyasSzoba('40', '2100'))

    def ui_prompt(self):
        while True:
            print('1. Szobafoglalas')
            print('2. Foglalas lemondasa')
            print('3. Szabad szobak listazasa')
            print('4. Szoba aranak lekerdezese')
            print('5. Kilepes')

            kivalasztott_opcio = input('Kerem valasszon a fenti opciok kozul: ')

            if kivalasztott_opcio == '1':
                szobaszam = input('Kerem adja meg a lefoglalni kivant szoba szamat: ')
                self.szalloda.szobafoglalas_szam_szerint(szobaszam)
            elif kivalasztott_opcio == '2':
                szobaszam = input('Kerem adja meg a lemondani kivant szoba szamat: ')
                self.szalloda.szamszerinti_foglalas_torlese(szobaszam)
            elif kivalasztott_opcio == '3':
                print('Szabad szobak:', self.szalloda.szabad_szobak_lekerdezese())
            elif kivalasztott_opcio == '4':
                print('Szoba arak:', self.szalloda.ar_lekerdezese())
            else:
                break


foglalas = Foglalas()
foglalas.szoba_adatok()
foglalas.ui_prompt()
