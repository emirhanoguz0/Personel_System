from personel import Personel

class Hemşire(Personel):
    def __init__(self,personel_no,isim,soyad,departman,maas,calisma_saati,sertifika,hastane):
        super().__init__(personel_no,isim,soyad,departman,maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def getCalismaSaati(self):
        return self.__calisma_saati

    def getSertifika(self):
        return self.__sertifika

    def getHastane(self):
        return self.__hastane

    def setCalismaSaati(self,saat):
        self.__calisma_saati = saat

    def setSertifika(self,sertifika):
        self.__sertifika = sertifika

    def setHastane(self,hastane):
        self.__hastane = hastane

    def __str__(self):
        return f"Calisma saati: {self.__calisma_saati} \nSertifika: {self.__sertifika} \nHastane: {self.__hastane}"

    def maas_arttir(self):
        return self.maas