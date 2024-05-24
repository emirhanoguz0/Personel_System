from personel import Personel
from doktor import Doktor
from hemşire import Hemşire
from hasta import Hasta
import pandas as pd
def main():
    p1= Personel(123123,"Ayça","Uçar","güvenlik",30000)
    p2= Personel(456456,"Samed","Ak","temizlik",20000)

    d1 = Doktor(789789,"Ege","Bulut","Kardiyoloji",50000,"Kardiyalog",7,"Atatürk Devlet Hastanesi")
    d2 = Doktor(741741,"Berkin","Yalcin","Nöroloji",70000,"Nörolog",5,"Özel Doğa Hastanesi")
    d3 = Doktor(852852,"Berkcan","Yıldız","Pediatri",60000,"Pediatri",6,"Özel Yeşil Hastanesi")

    h1 = Hemşire(963963,"İsmail","Özgüç","",45000,8,"Öfke Yönetimi","İzmir Devlet Hastanesi")
    h2 = Hemşire(321321,"Akif","Demir","",80000,7,"Yoğun Bakım","Özel Sağlık Hastanesi")
    h3 = Hemşire(654654,"Anıl","Sümerbaş","",40000,10,"Acil Bakım","Profesör Doktor Ali Devlet Hastanesi")

    hs1 = Hasta(987987,"Atakan","Oguz","20.05.1989","Grip","İlaç")
    hs2 = Hasta(753753,"Mert","Siliv","02.08.2000","Apandisit","Ameliyat")
    hs3 = Hasta(159159,"Eymen","Arı","03.05.2009","Sol sol kırılması","Dinlenme")

    #isimler = pd.Series(hs1.getAd(),hs2.getAd(),hs3.getAd())
    print(d1.getisim())

main()