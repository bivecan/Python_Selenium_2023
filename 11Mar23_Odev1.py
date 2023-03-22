ogrenciler = []

def ogrenciEkle():
    isim = input("Eklenecek ogrenci ismini giriniz:")
    ogrenciler.append(isim)
    print(ogrenciler)

def ogrenciSil():
    ad = input("Silinecek ogrenci ismini giriniz:")
    ogrenciler.remove(ad)
    print(ogrenciler)

def ogrencilerEkle():
    x = int(input("Kaç ogrenci ismi gireceksiniz:"))
    for i in range(x):
        ogrenciEkle()
        
def ogrenciYazdir():
    for ogrenci in ogrenciler:
        print(ogrenci)

def ogrenciNo():
    ogrenciIsim = input("Numarasını ogrenmek istediginiz ogrenci ismini girin:")
    for i in range(len(ogrenciler)):
        if ogrenciler[i] == ogrenciIsim:
            print(i)
    
def ogrencilerSil():
    while len(ogrenciler) != 0:
        ogrenciErase = input("Silinecek ogrenci ismini giriniz:")
        ogrenciler.remove(ogrenciErase)
        print(ogrenciler)

