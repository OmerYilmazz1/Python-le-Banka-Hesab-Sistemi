class BankaHesabi:
    def __init__(self , hesapSahibi , bakiye):
        self._hesapSahibi = hesapSahibi
        self._bakiye = bakiye

    @property
    def sahip(self):
        return self._hesapSahibi
    
    @sahip.setter
    def sahip(self , sahip):
        self._hesapSahibi = sahip

    @property
    def bakiye(self):
        return self._bakiye
    
    @bakiye.setter
    def bakiye(self , bakiye):
        self._bakiye = bakiye

    def para_cek(self , miktar):
        if(miktar > self._bakiye):
            print("Para Çekme İşlemi Başarısız Yetersiz Bakiye !!")
        else:
            self.bakiye = self._bakiye - miktar
            print(f"Para Çekildi Yeni Bakiye : {self.bakiye}")

    def para_yatir(self , miktar):
        self.bakiye = self._bakiye + miktar
        print(f"Para Yatırıldı Yeni Bakiye : {self.bakiye}")

isim = input("İsminizi Giriniz : ")
bakiye = int(input("Başlangıç Bakiyesini Belirleyin : "))
banka = BankaHesabi(isim , bakiye)

while True:
    print("-----------------------------------")
    print(f"!!!! Sayın {banka.sahip} ,  BANKAYA HOŞGELDİNİZ !!!!")
    print("1 - Para Yatır")
    print("2 - Para Çek")
    print("3 - Hesap Bilgilerini Göster")
    print("4 - Bankadaki Toplam Parayı Gör")
    print("5 - Çıkış")

    secim = int(input("Lütfen Yapacağınız İşlemi Seçiniz : "))

    if(secim == 1):
        yatir_miktar = int(input("Ne Kadar Para Yatırmak İstiyorsunuz : "))
        if(yatir_miktar < 0):
            print("Lütfen Geçerli Değer Giriniz !")
        else:
            banka.para_yatir(yatir_miktar)
    elif(secim == 2):
        cek_miktar = int(input("Ne Kadar Para Çekmek İstiyorsunuz : "))
        banka.para_cek(cek_miktar)
    elif(secim == 3):
        print(f"Adınız : {banka.sahip}  Bakiyeniz : {banka.bakiye}")
    elif(secim == 4):
        print(f"Bankadaki Toplam Para : {banka.bakiye}")
    elif(secim == 5):
        print(f"Çıkış Yapılıyor...")
        break