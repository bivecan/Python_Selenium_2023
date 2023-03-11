""" 
Python Veri Tipleri

1. Numbers: Sayısal her türlü değeri saklar.
   Kendi içinde alt tanımları: integer(tamsayılar), float(ondalıklı sayılar), complex(reel sayılar)

2. Strings: Öncelikli text değerlerini saklar. 
   Fakat sayısal değerler de String haline çevrilebilir. 

3. Lists: Bileşik veri tipidir.
   Farklı veya aynı tipte 1 veya daha fazla değeri birarada saklar.
   List yaratıldıktan sonra güncellenebilir. 

4. Tuples: Bileşik veri tipidir.
   Farklı veya aynı tipte 1 veya daha fazla değeri birarada saklar.
   Tuple yaratıldıktan sonra güncellenemez.

5. Dictionary: Bileşik veri tipidir, bir çeşit hash tablo türüdür.
   İçindeki değerlerin herbirine bir anahtar(key) atanır. Key sayesinde veriye hızlıca ulaşılır.

***********************************************************************************************************
Kodlama.io Sitesindeki Değişkenler

String  örnekler: "Kurslarım", "Tüm Kurslar", "Kariyer" alt başlıkları
Integer örnekler: Dersin tamamlanma yüzdesi, yorumların adedi
List    örnekler: Eğitmen(List'in değerleri:Tümü,Engin Demirog,Halit Enes Kalaycı)

************************************************************************************************************
Kodlama.io Sitesindeki Şart Blokları

Kullanıcı girişi yapıldıktan sonra AnaSayfada "(2023)Yazılım Geliştirici Yetiştirme Kampı-Python & Selenium"
 seçilip "Ders Progamı" tıklandığını düşünelim. 


tamamlanmaYuzdesi = 0

gun1DersProgramiBitir&DevamEt = False

#Ders Programı sayfası bitirilip devam edilecekse "Bitir ve Devam Et" butonu tıklanacak ve değeri True olacak.

gun1DersProgramiBitir&DevamEt = True

if gun1DersProgramiBitir&DevamEt:
   tamamlanmaYuzdesi = 25
   Goto page Degerlendirme

gun1DegerlendirmeBitir&DevamEt = False   

#Degerlendirme sayfası bitirilip devam edilecekse "Bitir ve Devam Et" butonu tıklanacak ve değeri True olacak.

gun1DegerlendirmeBitir&DevamEt = True

if gun1DegerlendirmeBitir&DevamEt:
   tamamlanmaYuzdesi = 50
   Goto page Odev1

gun1Odev1Bitir&DevamEt = False

#Odev1 sayfası bitirilip devam edilecekse "Bitir ve Devam Et" butonu tıklanacak ve değeri True olacak.

gun1Odev1Bitir&DevamEt = True

if gun1Odev1Bitir&DevamEt:
   tamamlanmaYuzdesi = 75
   Goto page Odev2

gun1Odev2Bitir&DevamEt = False

#Odev2 sayfası bitirilip devam edilecekse "Bitir ve Devam Et" butonu tıklanacak ve değeri True olacak.

gun1Odev2Bitir&DevamEt = True

if gun1Odev2Bitir&DevamEt:
   tamamlanmaYuzdesi = 100
   

"""