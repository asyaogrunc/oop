class Urun:
    def __init__(self, ad, fiyat, stok):
        self.ad = ad
        self.fiyat = fiyat
        self.stok = stok

    def __str__(self):
        return f"{self.ad} - {self.fiyat} TL (Stok: {self.stok})"

    def stok_guncelle(self, miktar):
        """Ürünün stok miktarını günceller."""
        if miktar > self.stok:
            return False
        self.stok -= miktar
        return True


class Musteri:
    def __init__(self, ad, e_posta):
        self.ad = ad
        self.e_posta = e_posta

    def __str__(self):
        return f"{self.ad} ({self.e_posta})"


class Sepet:
    def __init__(self):
        self.urunler = {}

    def urun_ekle(self, urun, miktar):
        """Sepete ürün ekler."""
        if miktar > urun.stok:
            print(f"Yetersiz stok! {urun.ad} için sadece {urun.stok} adet mevcut.")
            return
        if urun in self.urunler:
            self.urunler[urun] += miktar
        else:
            self.urunler[urun] = miktar
        urun.stok_guncelle(miktar)

    def urun_cikar(self, urun, miktar):
        """Sepetten ürün çıkarır."""
        if urun in self.urunler and self.urunler[urun] >= miktar:
            self.urunler[urun] -= miktar
            urun.stok += miktar
            if self.urunler[urun] == 0:
                del self.urunler[urun]
        else:
            print("Geçerli bir miktar girin veya ürün sepette bulunmuyor!")

    def sepeti_goruntule(self):
        """Sepeti görüntüler."""
        if not self.urunler:
            print("Sepetiniz boş.")
            return
        toplam = 0
        for urun, miktar in self.urunler.items():
            print(f"{urun.ad} - {miktar} adet - {urun.fiyat * miktar} TL")
            toplam += urun.fiyat * miktar
        print(f"\nToplam: {toplam} TL")


class Siparis:
    def __init__(self, musteri, sepet):
        self.musteri = musteri
        self.sepet = sepet

    def siparisi_tamamla(self):
        """Siparişi tamamlar ve sepeti temizler."""
        print(f"\nSipariş Tamamlandı!\nMüşteri: {self.musteri}\n")
        self.sepet.sepeti_goruntule()
        self.sepet.urunler.clear()  # Sepeti temizle


def main():
    urunler = [
        Urun("Laptop", 15000, 5),
        Urun("Telefon", 10000, 10),
        Urun("Kulaklık", 500, 20)
    ]

    # Müşteri bilgileri alınır
    ad = input("Müşteri Adınızı Girin: ")
    e_posta = input("E-posta adresinizi girin: ")
    musteri = Musteri(ad, e_posta)

    # Sepet oluşturuluyor
    sepet = Sepet()

    while True:
        print("\nÜrünler:")
        for i, urun in enumerate(urunler):
            print(f"{i+1}. {urun}")

        print("\nYapmak İstediğiniz İşlemi Seçiniz:")
        print("1. Ürün ekle")
        print("2. Ürün çıkar")
        print("3. Sepeti görüntüle")
        print("4. Siparişi Tamamla")
        print("5. Çıkış")

        secim = input("Seçiminizi Yapın: ")

        if secim == "1":
            try:
                urun_indeksi = int(input("Hangi ürünü eklemek istiyorsunuz? (Numara): ")) - 1
                if 0 <= urun_indeksi < len(urunler):
                    miktar = int(input("Kaç adet eklemek istiyorsunuz?: "))
                    sepet.urun_ekle(urunler[urun_indeksi], miktar)
                else:
                    print("Geçersiz ürün numarası!")
            except ValueError:
                print("Geçersiz giriş, tekrar deneyin!")

        elif secim == "2":
            try:
                urun_indeksi = int(input("Hangi ürünü çıkarmak istiyorsunuz? (Numara): ")) - 1
                if 0 <= urun_indeksi < len(urunler):
                    miktar = int(input("Kaç adet çıkarmak istiyorsunuz?: "))
                    sepet.urun_cikar(urunler[urun_indeksi], miktar)
                else:
                    print("Geçersiz ürün numarası!")
            except ValueError:
                print("Geçersiz giriş, tekrar deneyin!")

        elif secim == "3":
            sepet.sepeti_goruntule()

        elif secim == "4":
            siparis = Siparis(musteri, sepet)
            siparis.siparisi_tamamla()
            break  # Sipariş tamamlandığında çıkış yapılır

        elif secim == "5":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim, tekrar deneyin!")


if __name__ == "__main__":
    main()
