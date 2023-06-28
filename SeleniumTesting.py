#AKSA HİSSESİNİN FİYATI
#driver.get("")
#driver.implicitly_wait(20)
#bimasfiyat = driver.find_element(By.XPATH, '').text
#bimasfiyat = bimasfiyat.replace(",",".")

#1   HİSSESİ
#new_row = {
#    "Hisse": "",
#    "Hisse sayısı" : ,
#    "Alış Fiyatı(ort.)": ,
#    "Güncel satış fiyatı": ,
#    "Toplam Kar": (float() - ) * 
#}
#df1 = pandas.DataFrame([new_row])

import openpyxl 
import pandas
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

maddeler = ["Hisse","Hisse sayısı", "Alış Fiyatı(ort.)","Güncel satış fiyatı", "Toplam Kar","Güncel Toplam Fiyat","Yüzdelik Kar Oranı"]
#********************************************************************************************************************************************
#BAŞLANGIÇTA SORULMASI GEREKEN SORULAR

#1 FROTO BİLGİ ÇEKME
while True:
    try:
        froto_sayısı = int(input("Kaç FROTO hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
while True:
    try:
        froto_user_input = input("FROTO ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        froto_user_input = froto_user_input.replace(",",".")
        froto_alış_ort = float(froto_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE: ")

#2 BİMAS BİLGİ ÇEKME
while True:
    try:
        bimas_sayısı = int(input("Kaç BİMAS hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
while True:
    try:
        bimas_user_input = input("BİMAS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        bimas_user_input = bimas_user_input.replace(",",".")
        bimas_alış_ort = float(bimas_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE: ")

#3 TUPRS BİLGİ ÇEKME
while True:
    try:
        tuprs_sayısı = int(input("Kaç TUPRS hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")       
while True:
    try:
        tuprs_user_input = input("TUPRS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        tuprs_user_input = tuprs_user_input.replace(",",".")
        tuprs_alış_ort = float(tuprs_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE: ")

#4 AKSA BİLGİ ÇEKME
while True:
    try:
        aksa_sayısı = int(input("Kaç AKSA hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
while True:
    try:
        aksa_user_input = input("AKSA ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        aksa_user_input = aksa_user_input.replace(",",".")
        aksa_alış_ort = float(aksa_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE: ")

#5 KORDS BİLGİ ÇEKME
while True:
    try:
        kords_sayısı = int(input("Kaç KORDS hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
while True:
    try:
        kords_user_input = input("KORDS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        kords_user_input = kords_user_input.replace(",",".")
        kords_alış_ort = float(kords_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE: ")

#6 EREGL BİLGİ ÇEKME
while True:
    try:
        eregl_sayısı = int(input("Kaç EREGL hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
while True:
    try:
        eregl_user_input = input("EREGL ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        eregl_user_input = eregl_user_input.replace(",",".")
        eregl_alış_ort = float(eregl_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE: ")

#7 ASTOR BİLGİ ÇEKME
while True:
    try:
        astor_sayısı = int(input("Kaç ASTOR hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
while True:
    try:
        astor_user_input = input("ASTOR ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        astor_user_input = astor_user_input.replace(",",".")
        astor_alış_ort = float(astor_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE: ")

#8 BİOEN BİLGİ ÇEKME
while True:
    try:
        bioen_sayısı = int(input("Kaç BİOEN hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
while True:
    try:
        bioen_user_input = input("BİOEN ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        bioen_user_input = bioen_user_input.replace(",",".")
        bioen_alış_ort = float(bioen_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE: ")

#9 SOKE BİLGİ ÇEKME
while True:
    try:
        soke_sayısı = int(input("Kaç SOKE hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
while True:
    try:
        soke_user_input = input("SOKE ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        soke_user_input = soke_user_input.replace(",",".")
        soke_alış_ort = float(soke_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE: ")

#10 VESBE BİLGİ ÇEKME
while True:
    try:
        vesbe_sayısı = int(input("Kaç VESBE hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
while True:
    try:
        vesbe_user_input = input("VESBE ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        vesbe_user_input = vesbe_user_input.replace(",",".")
        vesbe_alış_ort = float(vesbe_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

#11 ALFAS BİLGİ ÇEKME
while True: 
    try:
        alfas_sayısı = int(input("Kaç ALFAS hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
        
while True: 
    try:
        alfas_user_input = input("ALFAS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        alfas_user_input = alfas_user_input.replace(",",".")
        alfas_alış_ort = float(alfas_user_input)
        break
    except ValueError:
        print("ALFAS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#12  BİLGİ ÇEKME
while True: 
    try:
        toasosayısı = int(input("Kaç TOASO hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
        
while True: 
    try:
        toaso_user_input = input("TOASO ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        toaso_user_input = toaso_user_input.replace(",",".")
        toaso_alış_ort = float(toaso_user_input)
        break
    except ValueError:
        print("TOASO ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#********************************************************************************************************************************************
#--------------------------------------------------------------------------------------------------------------------------------------------
df = pandas.DataFrame(columns=maddeler)
df
#--------------------------------------------------------------------------------------------------------------------------------------------
#+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+----+-+-+-+-+-+-+-+++-+--+-+-+-+-+-+--+-+-+-+-+-+++-+-++-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++
edge_options = Options()
edge_options.add_argument("--incognito")
edge_options.add_argument("--headless")  # Headless modu etkinleştirdim

driver = webdriver.Edge(options=edge_options)

driver.delete_all_cookies()
#+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+----+-+-+-+-+-+-+-+++-+--+-+-+-+-+-+--+-+-+-+-+-+++-+-++-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++
#############################################################################################################################################
#1 FROTO HİSSESİNİN FİYATI
driver.get("https://www.foreks.com/sembol-detay/H2024/froto/ford-otosan")
driver.implicitly_wait(20)
frotofiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
frotofiyat = frotofiyat.replace(",",".")

#2 BİMAS HİSSESİNİN FİYATI 
driver.get("https://www.foreks.com/sembol-detay/H1946/bimas/bim-magazalar")
driver.implicitly_wait(20)
bimasfiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
bimasfiyat = bimasfiyat.replace(",",".")

#3 TUPRS HİSSESİNİN FİYATI
driver.get("https://www.foreks.com/sembol-detay/H2122/tuprs/tupras")
driver.implicitly_wait(20)
tuprsfiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
tuprsfiyat = tuprsfiyat.replace(",",".")

#4 AKSA HİSSESİNİN FİYATI
driver.get("https://www.foreks.com/sembol-detay/H2892/aksa/aksa")
driver.implicitly_wait(20)
aksafiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
aksafiyat = aksafiyat.replace(",",".")

#5 KORDS HİSSESİNİN FİYATI
driver.get("https://www.foreks.com/sembol-detay/H2126/kords/kordsa-teknik-tekstil")
driver.implicitly_wait(20)
kordsfiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
kordsfiyat = kordsfiyat.replace(",",".")

#6 EREGL HİSSESİNİN FİYATI
driver.get("https://www.foreks.com/sembol-detay/H2674/eregl/eregli-demir-celik")
driver.implicitly_wait(20)
ereglfiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
ereglfiyat = ereglfiyat.replace(",",".") 

#7 ASTOR HİSSESİNİN FİYATI
driver.get("https://www.foreks.com/sembol-detay/H1461005/astor/astor-enerji")
driver.implicitly_wait(20)
astorfiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
astorfiyat = astorfiyat.replace(",",".")

#8 BİOEN HİSSESİNİN FİYATI
driver.get("https://www.foreks.com/sembol-detay/H830949/bioen/biotrend-cevre-ve-enerji")
driver.implicitly_wait(20)
bioenfiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
bioenfiyat = bioenfiyat.replace(",",".")

#9 SOKE HİSSESİNİN FİYATI
driver.get("https://www.foreks.com/sembol-detay/H1452897/soke/soke-degirmencilik")
driver.implicitly_wait(20)
sokefiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
sokefiyat = sokefiyat.replace(",",".")

#10 VESBE HİSSESİNİN FİYATI
driver.get("https://www.foreks.com/sembol-detay/H2888/vesbe/vestel-beyaz-esya")
driver.implicitly_wait(20)
vesbefiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
vesbefiyat = vesbefiyat.replace(",",".")

#11 ALFAS HİSSESİNİN FİYATI
driver.get("https://foreks.com/sembol-detay/H1388185/ALFAS/alfa-solar-enerji")
driver.implicitly_wait(20)
alfasfiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
alfasfiyat = alfasfiyat.replace(",",".")

#12 TOASO HİSSESİNİN FİYATI 
driver.get("https://foreks.com/sembol-detay/H2108/toaso/tofas-oto-fab")
driver.implicitly_wait(20)
toasofiyat = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong').text
toasofiyat = toasofiyat.replace(",",".")
#############################################################################################################################################
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#BURADA KODU DÖNGÜYE SOToplam KarAK FİYATLARI GİRMESİNİ İSTİYORUZ(ELLE GİRSEM DAHA İYİ OLABİLİR BELKİ)
#1 FROTO HİSSESİ
froto_Kar = float(frotofiyat) - froto_alış_ort 
new_row1 = {
    "Hisse": "FROTO",
    "Hisse sayısı" : froto_sayısı,
    "Alış Fiyatı(ort.)": froto_alış_ort,
    "Güncel satış fiyatı": frotofiyat,
    "Toplam Kar": (float(frotofiyat) - froto_alış_ort) * froto_sayısı,
    "Güncel Toplam Fiyat": froto_sayısı * float(frotofiyat),
    "Yüzdelik Kar Oranı" : (froto_Kar/float(frotofiyat)) * 100
}
df1 = pandas.DataFrame([new_row1])

#2 BİMAS HİSSESİ
bimas_Kar = float(bimasfiyat) - bimas_alış_ort
new_row2 = {
    "Hisse": "BİMAS",
    "Hisse sayısı" : bimas_sayısı,
    "Alış Fiyatı(ort.)": bimas_alış_ort,
    "Güncel satış fiyatı": bimasfiyat,
    "Toplam Kar": (float(bimasfiyat) - bimas_alış_ort)*bimas_sayısı,
    "Güncel Toplam Fiyat": bimas_sayısı * float(bimasfiyat),
    "Yüzdelik Kar Oranı" : (bimas_Kar/float(bimasfiyat)) * 100
}
df2 = pandas.DataFrame([new_row2])

#3 TUPRS HİSSESİ
tuprs_Kar = float(tuprsfiyat) - tuprs_alış_ort
new_row3 = {
    "Hisse": "TUPRS",
    "Hisse sayısı" : tuprs_sayısı,
    "Alış Fiyatı(ort.)": tuprs_alış_ort,
    "Güncel satış fiyatı": tuprsfiyat,
    "Toplam Kar": (float(tuprsfiyat) - tuprs_alış_ort ) * tuprs_sayısı,
    "Güncel Toplam Fiyat": tuprs_sayısı * float(tuprsfiyat),
    "Yüzdelik Kar Oranı" : (tuprs_Kar/float(tuprsfiyat)) * 100
}
df3 = pandas.DataFrame([new_row3])

#4 AKSA HİSSESİ
aksa_Kar = float(aksafiyat) - aksa_alış_ort
new_row4 = {
    "Hisse": "AKSA",
    "Hisse sayısı" : aksa_sayısı,
    "Alış Fiyatı(ort.)": aksa_alış_ort,
    "Güncel satış fiyatı": aksafiyat,
    "Toplam Kar": (float(aksafiyat) - aksa_alış_ort) * aksa_sayısı,
    "Güncel Toplam Fiyat": aksa_sayısı * float(aksafiyat),
    "Yüzdelik Kar Oranı" : (aksa_Kar/float(aksafiyat)) * 100
}
df4 = pandas.DataFrame([new_row4])

#5 KORDS HİSSESİ
kords_Kar = float(kordsfiyat) - kords_alış_ort
new_row5 = {
    "Hisse": "KORDS",
    "Hisse sayısı" : kords_sayısı,
    "Alış Fiyatı(ort.)": kords_alış_ort,
    "Güncel satış fiyatı": kordsfiyat,
    "Toplam Kar": (float(kordsfiyat) - kords_alış_ort) * kords_sayısı,
    "Güncel Toplam Fiyat": kords_sayısı * float(kordsfiyat),
    "Yüzdelik Kar Oranı" : (kords_Kar/float(kordsfiyat)) * 100
}
df5 = pandas.DataFrame([new_row5])

#6 EREGL HİSSESİ
eregl_Kar = float(ereglfiyat) - eregl_alış_ort
new_row6 = {
    "Hisse": "EREGL",
    "Hisse sayısı" : eregl_sayısı ,
    "Alış Fiyatı(ort.)": eregl_alış_ort ,
    "Güncel satış fiyatı": ereglfiyat,
    "Toplam Kar": (float(ereglfiyat) - eregl_alış_ort ) * eregl_sayısı,
    "Güncel Toplam Fiyat": eregl_sayısı * float(ereglfiyat),
    "Yüzdelik Kar Oranı" : (eregl_Kar/float(ereglfiyat)) * 100
}
df6 = pandas.DataFrame([new_row6])

#7 ASTOR  HİSSESİ
astor_Kar = float(astorfiyat) - astor_alış_ort
new_row7 = {
    "Hisse": "ASTOR",
    "Hisse sayısı" : astor_sayısı ,
    "Alış Fiyatı(ort.)": astor_alış_ort,
    "Güncel satış fiyatı": astorfiyat,
    "Toplam Kar": (float(astorfiyat) - astor_alış_ort) * astor_sayısı,
    "Güncel Toplam Fiyat": astor_sayısı * float(astorfiyat),
    "Yüzdelik Kar Oranı" : (astor_Kar/float(astorfiyat)) * 100
}
df7 = pandas.DataFrame([new_row7])

#8 BİOEN  HİSSESİ
bioen_Kar = float(bioenfiyat) - bioen_alış_ort
new_row8 = {
    "Hisse": "BİOEN",
    "Hisse sayısı" : bioen_sayısı,
    "Alış Fiyatı(ort.)": bioen_alış_ort,
    "Güncel satış fiyatı": bioenfiyat,
    "Toplam Kar": (float(bioenfiyat) - bioen_alış_ort ) * bioen_sayısı,
    "Güncel Toplam Fiyat": bioen_sayısı * float(bioenfiyat),
    "Yüzdelik Kar Oranı" : (bioen_Kar/float(bioenfiyat)) * 100
}
df8 = pandas.DataFrame([new_row8]) 

#9 SOKE  HİSSESİ
soke_Kar = float(sokefiyat) - soke_alış_ort
new_row9 = {
    "Hisse": "SOKE",
    "Hisse sayısı" : soke_sayısı,
    "Alış Fiyatı(ort.)": soke_alış_ort ,
    "Güncel satış fiyatı": sokefiyat,
    "Toplam Kar": (float(sokefiyat) - soke_alış_ort ) * soke_sayısı,
    "Güncel Toplam Fiyat": soke_sayısı * float(sokefiyat),
    "Yüzdelik Kar Oranı" : (soke_Kar/float(sokefiyat)) * 100
}
df9 = pandas.DataFrame([new_row9])

#10 VESBE HİSSESİ
vesbe_Kar = float(vesbefiyat) - vesbe_alış_ort
new_row10 = {
    "Hisse": "VESBE",
    "Hisse sayısı" : vesbe_sayısı ,
    "Alış Fiyatı(ort.)": vesbe_alış_ort,
    "Güncel satış fiyatı": vesbefiyat,
    "Toplam Kar": (float(vesbefiyat) - vesbe_alış_ort) * vesbe_sayısı,
    "Güncel Toplam Fiyat": vesbe_sayısı * float(vesbefiyat),
    "Yüzdelik Kar Oranı" : (vesbe_Kar/float(vesbefiyat)) * 100
}
df10 = pandas.DataFrame([new_row10])

#11 ALFAS HİSSESİ
alfas_Kar = float(alfasfiyat) - alfas_alış_ort
new_row11 = {
    "Hisse": "ALFAS",
    "Hisse sayısı" : alfas_sayısı,
    "Alış Fiyatı(ort.)": alfas_alış_ort,
    "Güncel satış fiyatı": alfasfiyat,
    "Toplam Kar": (float(alfasfiyat) - alfas_alış_ort) * alfas_sayısı,
    "Güncel Toplam Fiyat": alfas_sayısı * float(alfasfiyat),
    "Yüzdelik Kar Oranı" : (alfas_Kar/float(alfasfiyat)) * 100
}
df11 = pandas.DataFrame([new_row11])

#12 TOASO HİSSESİ
toaso_Kar = float(toasofiyat) -toaso_alış_ort
new_row12 = {
    "Hisse": "TOASO",
    "Hisse sayısı" : toasosayısı ,
    "Alış Fiyatı(ort.)": toaso_alış_ort,
    "Güncel satış fiyatı": toasofiyat,
    "Toplam Kar": (float(toasofiyat) - toaso_alış_ort) * toasosayısı,
    "Güncel Toplam Fiyat": toasosayısı * float(toasofiyat),
    "Yüzdelik Kar Oranı" : (toaso_Kar/float(toasofiyat)) * 100
}
df12 = pandas.DataFrame([new_row12])
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# DataFrame'leri birleştir
df = pandas.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12], ignore_index=True)

#OLŞACAK DOSYAIN ADINI BELİRLEME
while True: 
    DosyaAdı = input("OLUŞACAK DOSYAININ ADINI BELİRLE: ")
    if "\\ " in DosyaAdı or "/ " in DosyaAdı or ":" in DosyaAdı or  "*" in DosyaAdı or "<" in DosyaAdı or ">" in DosyaAdı :
        print('GEÇERSİZ Toplam KarAKTERLERİ KULLANMA! (   \  /  :  *  ?  "  <  >   )')
    else: 
        break

# Excel dosyasına yaz
df.to_excel("D:/Düzenli Masaüstü Remote/Excel & Borsa.py/ciktilar/{}.xlsx".format(DosyaAdı), index=False)

print("OLUŞAN DOSYAYI BU ADRESTEN BULABİLİRSİN: D:/Düzenli Masaüstü Remote/Excel & Borsa.py/ciktilar/{}.xlsx".format(DosyaAdı))

#TO DO:       Güncel Toplam Fiyat Toplam KarLARI TOPLAYIP EXCELDE YENİ BİR ROW'DA YAZAN KOMUT YAZ!! +++ tamamlandı +++
