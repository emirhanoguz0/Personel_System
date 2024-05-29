class Hasta:
    def __init__(self,hasta_no,ad,soyad,dogum_tarihi,hastalik,tedavi):
        self.hasta_no = hasta_no
        self.ad = ad
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi
        self.hastalik = hastalik
        self.tedavi = tedavi

    def __str__(self):
        return f"HastaNo: {self.hasta_no} \nAd: {self.ad} \nSoyad: {self.soyad} \nDogum Tarihi: {self.dogum_tarihi} \nHastalik: {self.hastalik} \nTedavi: {self.tedavi}"

    def getHastaNo(self):
        return self.hasta_no

    def getAd(self):
        return self.ad

    def getSoyad(self):
        return self.soyad

    def getDogum_Tarihi(self):
        return self.dogum_tarihi

    def getHastalik(self):
        return self.hastalik

    def getTedavi(self):
        return self.tedavi

    def setHastaNo(self,hasta_no):
        self.hasta_no = hasta_no

    def setAd(self,ad):
        self.ad = ad

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