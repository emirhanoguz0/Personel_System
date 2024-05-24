from personel import Personel

class Doktor(Personel):
    def __init__(self,personel_no,isim,soyad,departman,maas,uzmanlik,deneyim_yili,hastane):
        super().__init__(personel_no,isim,soyad,departman,maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def getUzmanlik(self):
        return self.__uzmanlik

    def getDeneyimYili(self):
        return self.__deneyim_yili

    def getHastane(self):
        return self.__hastane

    def setUzmanlik(self,uzmanlik):
        self.__uzmanlik = uzmanlik

    def setDeneyimYili(self,deneyimYili):
        self.__deneyimYili = deneyimYili

    def setHastane(self):
        self.__hastane = hastane

    def __str__(self):
        return f"Uzmanlik: {self.__uzmanlik} \nDeneyimYili: {self.__deneyimYili} \nHastane: {self.__hastane}"

    def maas_arttir(self):
        return self.__maas