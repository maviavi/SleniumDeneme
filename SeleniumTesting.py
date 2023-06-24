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
#    "kar": (float() - ) * 
#}
#df1 = pandas.DataFrame([new_row])

import openpyxl 
import pandas
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

maddeler = ["Hisse","Hisse sayısı", "Alış Fiyatı(ort.)","Güncel satış fiyatı", "kar"]
#********************************************************************************************************************************************
#BAŞLANGIÇTA SORULMASI GEREKEN SORULAR

#1 FROTO BİLGİ ÇEKME
while True:
    try:
        froto_sayısı = int(input("Kaç FROTO hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE:")
while True:
    try:
        froto_user_input = input("FROTO ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        froto_user_input = froto_user_input.replace(",",".")
        froto_alış_ort = float(froto_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

#2 BİMAS BİLGİ ÇEKME
while True:
    try:
        bimas_sayısı = int(input("Kaç BİMAS hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE:")
while True:
    try:
        bimas_user_input = input("BİMAS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        bimas_user_input = bimas_user_input.replace(",",".")
        bimas_alış_ort = float(bimas_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

#3 TUPRS BİLGİ ÇEKME
while True:
    try:
        tuprs_sayısı = int(input("Kaç TUPRS hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE:")       
while True:
    try:
        tuprs_user_input = input("TUPRS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        tuprs_user_input = tuprs_user_input.replace(",",".")
        tuprs_alış_ort = float(tuprs_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

#4 AKSA BİLGİ ÇEKME
while True:
    try:
        aksa_sayısı = int(input("Kaç AKSA hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE:")
while True:
    try:
        aksa_user_input = input("AKSA ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        aksa_user_input = aksa_user_input.replace(",",".")
        aksa_alış_ort = float(aksa_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

#5 KORDS BİLGİ ÇEKME
while True:
    try:
        kords_sayısı = int(input("Kaç KORDS hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE:")
while True:
    try:
        kords_user_input = input("KORDS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        kords_user_input = kords_user_input.replace(",",".")
        kords_alış_ort = float(kords_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

#6 EREGL BİLGİ ÇEKME
while True:
    try:
        eregl_sayısı = int(input("Kaç EREGL hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE:")
while True:
    try:
        eregl_user_input = input("EREGL ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        eregl_user_input = eregl_user_input.replace(",",".")
        eregl_alış_ort = float(eregl_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

#7 ASTOR BİLGİ ÇEKME
while True:
    try:
        astor_sayısı = int(input("Kaç ASTOR hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE:")
while True:
    try:
        astor_user_input = input("ASTOR ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        astor_user_input = astor_user_input.replace(",",".")
        astor_alış_ort = float(astor_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

#8 BİOEN BİLGİ ÇEKME
while True:
    try:
        bioen_sayısı = int(input("Kaç BİOEN hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE:")
while True:
    try:
        bioen_user_input = input("BİOEN ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        bioen_user_input = bioen_user_input.replace(",",".")
        bioen_alış_ort = float(bioen_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

#9 SOKE BİLGİ ÇEKME
while True:
    try:
        soke_sayısı = int(input("Kaç SOKE hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE:")
while True:
    try:
        soke_user_input = input("SOKE ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        soke_user_input = soke_user_input.replace(",",".")
        soke_alış_ort = float(soke_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

#10 VESBE BİLGİ ÇEKME
while True:
    try:
        vesbe_sayısı = int(input("Kaç VESBE hissen var? "))
        break
    except ValueError:
        print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE:")
while True:
    try:
        vesbe_user_input = input("VESBE ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
        vesbe_user_input = vesbe_user_input.replace(",",".")
        vesbe_alış_ort = float(vesbe_user_input)
        break
    except ValueError:
        print("METİNSEL DEĞER GİRİLEMEZ! TEKRAR DENE:")

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
#############################################################################################################################################
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#BURADA KODU DÖNGÜYE SOKARAK FİYATLARI GİRMESİNİ İSTİYORUZ(ELLE GİRSEM DAHA İYİ OLABİLİR BELKİ)
#1 FROTO HİSSESİ
new_row1 = {
    "Hisse": "FROTO",
    "Hisse sayısı" : froto_sayısı,
    "Alış Fiyatı(ort.)": froto_alış_ort,
    "Güncel satış fiyatı": frotofiyat,
    "kar": (float(frotofiyat) - froto_alış_ort) * froto_sayısı
}
df1 = pandas.DataFrame([new_row1])

#2 BİMAS HİSSESİ
new_row2 = {
    "Hisse": "BİMAS",
    "Hisse sayısı" : bimas_sayısı,
    "Alış Fiyatı(ort.)": bimas_alış_ort,
    "Güncel satış fiyatı": bimasfiyat,
    "kar": (float(bimasfiyat) - bimas_alış_ort)*bimas_sayısı
}
df2 = pandas.DataFrame([new_row2])

#3 TUPRS HİSSESİ
new_row3 = {
    "Hisse": "TUPRS",
    "Hisse sayısı" : tuprs_sayısı,
    "Alış Fiyatı(ort.)": tuprs_alış_ort,
    "Güncel satış fiyatı": tuprsfiyat,
    "kar": (float(tuprsfiyat) - tuprs_alış_ort ) * tuprs_sayısı
}
df3 = pandas.DataFrame([new_row3])

#4 AKSA HİSSESİ
new_row4 = {
    "Hisse": "AKSA",
    "Hisse sayısı" : aksa_sayısı,
    "Alış Fiyatı(ort.)": aksa_alış_ort,
    "Güncel satış fiyatı": aksafiyat,
    "kar": (float(aksafiyat) - aksa_alış_ort) * aksa_sayısı
}
df4 = pandas.DataFrame([new_row4])

#5 KORDS HİSSESİ
new_row5 = {
    "Hisse": "KORDS",
    "Hisse sayısı" : kords_sayısı,
    "Alış Fiyatı(ort.)": kords_alış_ort,
    "Güncel satış fiyatı": kordsfiyat,
    "kar": (float(kordsfiyat) - kords_alış_ort) * kords_sayısı
}
df5 = pandas.DataFrame([new_row5])

#6 EREGL HİSSESİ
new_row6 = {
    "Hisse": "EREGL",
    "Hisse sayısı" : eregl_sayısı ,
    "Alış Fiyatı(ort.)": eregl_alış_ort ,
    "Güncel satış fiyatı": ereglfiyat,
    "kar": (float(ereglfiyat) - eregl_alış_ort ) * eregl_sayısı
}
df6 = pandas.DataFrame([new_row6])

#7 ASTOR  HİSSESİ
new_row7 = {
    "Hisse": "ASTOR",
    "Hisse sayısı" : astor_sayısı ,
    "Alış Fiyatı(ort.)": astor_alış_ort,
    "Güncel satış fiyatı": astorfiyat,
    "kar": (float(astorfiyat) - astor_alış_ort) * astor_sayısı
}
df7 = pandas.DataFrame([new_row7])

#8 BİOEN  HİSSESİ
new_row8 = {
    "Hisse": "BİOEN",
    "Hisse sayısı" : bioen_sayısı,
    "Alış Fiyatı(ort.)": bioen_alış_ort,
    "Güncel satış fiyatı": bioenfiyat,
    "kar": (float(bioenfiyat) - bioen_alış_ort ) * bioen_sayısı
}
df8 = pandas.DataFrame([new_row8]) 

#9 SOKE  HİSSESİ
new_row9 = {
    "Hisse": "SOKE",
    "Hisse sayısı" : soke_sayısı,
    "Alış Fiyatı(ort.)": soke_alış_ort ,
    "Güncel satış fiyatı": sokefiyat,
    "kar": (float(sokefiyat) - soke_alış_ort ) * soke_sayısı
}
df9 = pandas.DataFrame([new_row9])

#10 VESBE HİSSESİ
new_row10 = {
    "Hisse": "VESBE",
    "Hisse sayısı" : vesbe_sayısı ,
    "Alış Fiyatı(ort.)": vesbe_alış_ort,
    "Güncel satış fiyatı": vesbefiyat,
    "kar": (float(vesbefiyat) - vesbe_alış_ort) * vesbe_sayısı
}
df10 = pandas.DataFrame([new_row10])
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# DataFrame'leri birleştir
df = pandas.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10], ignore_index=True)

#OLŞACAK DOSYAIN ADINI BELİRLEME
while True: 
    DosyaAdı = input("OLUŞACAK DOSYAININ ADINI BELİRLE: ")
    if "\\ " in DosyaAdı or "/ " in DosyaAdı or ":" in DosyaAdı or  "*" in DosyaAdı or "<" in DosyaAdı or ">" in DosyaAdı :
        print('GEÇERSİZ KARAKTERLERİ KULLANMA! (   \  /  :  *  ?  "  <  >   )')
    else: 
        break

# Excel dosyasına yaz
df.to_excel("D:/Düzenli Masaüstü Remote/Excel & Borsa.py/ciktilar/{}.xlsx".format(DosyaAdı), index=False)

print("OLUŞAN DOSYAYI BU ADRESTEN BULABİLİRSİN: D:/Düzenli Masaüstü Remote/Excel & Borsa.py/ciktilar/{}.xlsx".format(DosyaAdı))