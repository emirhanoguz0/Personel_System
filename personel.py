class Personel:
    def __init__(self, personel_no, isim, soyad, departman, maas):
        self.__personel_no = personel_no
        self.__isim = isim
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas

    def __str__(self):
        return f"Personel No: {self.__personel_no} \nİsim: {self.__isim} \nSoyad: {self.__soyad} \nDepartman: {self.__departman} \nMaas: {self.__maas}"

    def getpersonel_no(self):
        return self.__personel_no

    def getisim(self):
        return self.__isim

    def getsoyad(self):
        return self.__soyad

    def getdepartman(self):
        return self.__departman

    def getmaas(self):
        return self.__maas

    def setpersonel_no(self, no):
        self.__personel_no = no

    def setisim(self, isim):
        self.__isim = isim

    def setsoyad(self, soyad):
        self.__soyad = soyad

    def setdepartman(self, departman):
        self.__departman = departman

    def setmaas(self, maas):
        self.__maas = maas