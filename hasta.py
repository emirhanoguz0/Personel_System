class Hasta:
    def __init__(self,hasta_no,isim,soyad,dogum_yili,hastalik,tedavi):
        self.hasta_no = hasta_no
        self.isim = isim
        self.soyad = soyad
        self.dogum_yili = dogum_yili
        self.hastalik = hastalik
        self.tedavi = tedavi

    def __str__(self):
        return f"HastaNo: {self.hasta_no} \nAd: {self.ad} \nSoyad: {self.soyad} \nDogum Tarihi: {self.dogum_yili} \nHastalik: {self.hastalik} \nTedavi: {self.tedavi}"

    def getHastaNo(self):
        return self.hasta_no

    def getisim(self):
        return self.isim

    def getsoyad(self):
        return self.soyad

    def getDogum_Yili(self):
        return self.dogum_yili

    def getHastalik(self):
        return self.hastalik

    def getTedavi(self):
        return self.tedavi

    def setHastaNo(self,hasta_no):
        self.hasta_no = hasta_no

    def setisim(self,isim):
        self.isim = isim

    def setSoyad(self,soyad):
        self.soyad = soyad

    def setHastalik(self,hastalik):
        self.hastalik = hastalik

    def setTedavi(self,tedavi):
        self.tedavi = tedavi

    def tedavi_suresi_hesapla(self):
        if self.__tedavi == "İlaç":
            return "2 hafta"
        if self.__tedavi == "Ameliyat":
            return "4 ay"
        if self.__tedavi == "Dinlenme":
            return "1 ay"