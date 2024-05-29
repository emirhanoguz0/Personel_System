from personel import Personel
from doktor import Doktor
from hemşire import Hemşire
from hasta import Hasta
import pandas as pd

def kac_tane_bul(dicti,z):
    sayac = 0
    for i in dicti[z]:
        if dicti[z][i] != 0:
            sayac = sayac + 1
    return sayac
def main():

    p1= Personel(123123,"Ayça","Uçar","güvenlik",30000)
    p2= Personel(456456,"Samed","Ak","temizlik",20000)

    d1 = Doktor(789789,"Ege","Bulut","Kardiyoloji",50000,"Kardiyalog",7,"Atatürk Devlet Hastanesi")
    d2 = Doktor(741741,"Berkin","Yalcin","Nöroloji",70000,"Nörolog",5,"Özel Doğa Hastanesi")
    d3 = Doktor(852852,"Berkcan","Yıldız","Pediatri",60000,"Pediatri",6,"Özel Yeşil Hastanesi")

    h1 = Hemşire(963963,"İsmail","Özgüç","",45000,8,"Öfke Yönetimi","İzmir Devlet Hastanesi")
    h2 = Hemşire(321321,"Akif","Demir","Yoğun Bakim",80000,7,"Yoğun Bakim","Özel Sağlık Hastanesi")
    h3 = Hemşire(654654,"Anıl","Sümerbaş","Acil Bakim",40000,10,"Acil Bakim","Profesör Doktor Ali Devlet Hastanesi")

    hs1 = Hasta(987987,"Atakan","Oguz","20.05.1989","Grip","İlaç")
    hs2 = Hasta(753753,"Mert","Siliv","02.08.2000","Apandisit","Ameliyat")
    hs3 = Hasta(159159,"Serhat","Arı","03.05.2009","Sol sol kırılması","Dinlenme")

    p = [p1,p2,d1,d2,d3,h1,h2,h3,hs1,hs2,hs3]

    data = {
        "Personel No": [0] * len(p),
        "İsim": [0] * len(p),
        "Soyad": [0] * len(p),
        "Departman": [0] * len(p),
        "Maas": [0] * len(p),
        "Uzmanlık": [0] * len(p),
        "Deneyim Yılı": [0] * len(p),
        "Hastane": [0] * len(p),
        "Çalışma Saati": [0] * len(p),
        "Sertifika": [0] * len(p),
        "Hasta No": [0] * len(p),
        "Doğum Tarihi": [0] * len(p),
        "Hastalık": [0] * len(p),
        "Tedavi": [0] * len(p)
    }

    for i in range(len(p)):
        data['İsim'][i] = p[i].getisim()
        data['Soyad'][i] = p[i].getsoyad()

        if isinstance(p[i], Hasta):
            data['Hasta No'][i] = p[i].getHastaNo()
            data['Doğum Tarihi'][i] = p[i].getDogum_Tarihi()
            data['Hastalık'][i] = p[i].getHastalik()
            data['Tedavi'][i] = p[i].getTedavi()
        else:
            data['Personel No'][i] = p[i].getpersonel_no()
            data['Departman'][i] = p[i].getdepartman()
            data['Maas'][i] = p[i].getmaas()

        if isinstance(p[i], Doktor):
            data['Uzmanlık'][i] = p[i].getUzmanlik()
            data['Deneyim Yılı'][i] = p[i].getDeneyimYili()
            data['Hastane'][i] = p[i].getHastane()

        if isinstance(p[i], Hemşire):
            data['Çalışma Saati'][i] = p[i].getCalismaSaati()
            data['Sertifika'][i] = p[i].getSertifika()
            data['Hastane'][i] = p[i].getHastane()

    x = int(input("1-Tablo \n2-Deneyimli Doktor Sayisi \n3-Hasta Tablosu \n4-Maasi 7000den büyükler \n"))

    df = pd.DataFrame(data)

    if x == 1:
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        print(df)
    if x == 2:
        experienced_doctors = df[df['Deneyim Yılı'] > 5]
        print(len(experienced_doctors))
    if x == 3:
        hasta_df = df[df['Personel No'] == 0].sort_values(by='İsim')
        print(hasta_df)
    if x == 4:
        maas7k_df = df[df['Maas'] > 7000]
        print(maas7k_df[["Personel No","İsim","Soyad","Maas"]])

main()