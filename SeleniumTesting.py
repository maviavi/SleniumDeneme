#X HİSSESİNİN FİYATI
#driver.get("")
#driver.implicitly_wait(20)
#Xfiyat = driver.find_element(By.XPATH, '').text
#Xfiyat = Xfiyat.replace(",",".")

#Y X  HİSSESİ
#new_rowY = {
#    "Hisse": "X",
#    "Hisse sayısı" : ,
#    "Alış Fiyatı(ort.)": ,
#    "Güncel satış fiyatı": ,
#    "Toplam Kar": (float() - ) * 
#}
#dfY = pandas.DataFrame([new_rowY])

import openpyxl 
import pandas
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

maddeler = ["Hisse", "Hisse sayısı", "Alış Fiyatı(ort.)", "Güncel satış fiyatı", "Toplam Kar", "Güncel Toplam Fiyat", "Yüzdelik Kar Oranı"]
#********************************************************************************************************************************************
#BAŞLANGIÇTA SORULMASI GEREKEN SORULAR

def get_user_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except ValueError:
            print("ONDALIKLI SAYI VEYA METİN GİREMEZSİN! TEKRAR DENE: ")
    return value
#FONKSİYONLARLA TEKRARLI DÖNGÜLERDEN KURTUL(WHILE TRUE)
def get_user_float_input(fltprompt):
    while True:
        try:
            fltvalue = (input(fltprompt)).replace(",",".")
            fltvalue = float(fltvalue)
            break
        except ValueError:
            print("GEÇERSİZ GİRİŞ! SAYISAL BİR DEĞER GİR: ")
    return fltvalue

#1 FROTO BİLGİ ÇEKME
froto_sayısı = get_user_int_input("kaç FROTO hissen var? ")
froto_alış_ort = get_user_float_input("FROTO ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#2 BİMAS BİLGİ ÇEKME
bimas_sayısı = get_user_int_input("Kaç BİMAS hissen var? ")
bimas_alış_ort = get_user_float_input("BİMAS ALIŞ FİYATI ORTALAMAN KAÇ? ")

#3 TUPRS BİLGİ ÇEKME
tuprs_sayısı = get_user_int_input("Kaç TUPRS hissen var? ")
tuprs_alış_ort = get_user_float_input("TUPRS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#4 AKSA BİLGİ ÇEKME
aksa_sayısı = get_user_int_input("Kaç AKSA hissen var? ")
aksa_alış_ort = get_user_float_input("AKSA ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#5 KORDS BİLGİ ÇEKME
kords_sayısı = get_user_int_input("Kaç KORDS hissen var? ")
kords_alış_ort = get_user_float_input("KORDS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#6 EREGL BİLGİ ÇEKME
eregl_sayısı = get_user_int_input("Kaç EREGL hissen var? ")
eregl_alış_ort = get_user_float_input("EREGL ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#7 ASTOR BİLGİ ÇEKME
astor_sayısı = get_user_int_input("Kaç ASTOR hissen var? ")
astor_alış_ort = get_user_float_input("ASTOR ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#8 BİOEN BİLGİ ÇEKME
bioen_sayısı = get_user_int_input("Kaç BİOEN hissen var? ")
bioen_alış_ort = get_user_float_input("BİOEN ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#9 SOKE BİLGİ ÇEKME
soke_sayısı = get_user_int_input("Kaç SOKE hissen var? ")
soke_alış_ort = get_user_float_input("SOKE ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#10 VESBE BİLGİ ÇEKME
vesbe_sayısı = get_user_int_input("Kaç VESBE hissen var? ")
vesbe_alış_ort = get_user_float_input("VESBE ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#11 ALFAS BİLGİ ÇEKME
alfas_sayısı = get_user_int_input("Kaç ALFAS hissen var? ")
alfas_alış_ort = get_user_float_input("ALFAS ALIŞ FİYATI ORTALAMAN KAÇ TL? ")

#12  BİLGİ ÇEKME
toasosayısı = get_user_int_input("Kaç TOASO hissen var? ")
toaso_alış_ort = get_user_float_input("TOASO ALIŞ FİYATI ORTALAMAN KAÇ TL? ")
#********************************************************************************************************************************************

#+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+----+-+-+-+-+-+-+-+++-+--+-+-+-+-+-+--+-+-+-+-+-+++-+-++-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++
edge_options = Options()
edge_options.add_argument("--incognito") # gizli sekme
edge_options.add_argument("--headless")  # Tarayıcının görünmez modunu etkinleştirme

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
#MADDELERE DEĞERLERİ GİR
#1 FROTO HİSSESİ
froto_Kar = float(frotofiyat) - froto_alış_ort 
new_row1 = {
    "Hisse": "FROTO",
    "Hisse sayısı" : froto_sayısı,
    "Alış Fiyatı(ort.)": froto_alış_ort,
    "Güncel satış fiyatı": frotofiyat,
    "Güncel Toplam Fiyat": froto_sayısı * float(frotofiyat),
    "Toplam Kar": (float(frotofiyat) - froto_alış_ort) * froto_sayısı,
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
    "Güncel Toplam Fiyat": bimas_sayısı * float(bimasfiyat),
    "Toplam Kar": (float(bimasfiyat) - bimas_alış_ort)*bimas_sayısı,
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
    "Güncel Toplam Fiyat": tuprs_sayısı * float(tuprsfiyat),
    "Toplam Kar": (float(tuprsfiyat) - tuprs_alış_ort ) * tuprs_sayısı,
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
    "Güncel Toplam Fiyat": aksa_sayısı * float(aksafiyat),
    "Toplam Kar": (float(aksafiyat) - aksa_alış_ort) * aksa_sayısı,
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
    "Güncel Toplam Fiyat": kords_sayısı * float(kordsfiyat),
    "Toplam Kar": (float(kordsfiyat) - kords_alış_ort) * kords_sayısı,
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
    "Güncel Toplam Fiyat": eregl_sayısı * float(ereglfiyat),
    "Toplam Kar": (float(ereglfiyat) - eregl_alış_ort ) * eregl_sayısı,
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
    "Güncel Toplam Fiyat": astor_sayısı * float(astorfiyat),
    "Toplam Kar": (float(astorfiyat) - astor_alış_ort) * astor_sayısı,
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
    "Güncel Toplam Fiyat": bioen_sayısı * float(bioenfiyat),
    "Toplam Kar": (float(bioenfiyat) - bioen_alış_ort ) * bioen_sayısı,
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
    "Güncel Toplam Fiyat": soke_sayısı * float(sokefiyat),
    "Toplam Kar": (float(sokefiyat) - soke_alış_ort ) * soke_sayısı,
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
    "Güncel Toplam Fiyat": vesbe_sayısı * float(vesbefiyat),
    "Toplam Kar": (float(vesbefiyat) - vesbe_alış_ort) * vesbe_sayısı,
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
    "Güncel Toplam Fiyat": alfas_sayısı * float(alfasfiyat),
    "Toplam Kar": (float(alfasfiyat) - alfas_alış_ort) * alfas_sayısı,
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
    "Güncel Toplam Fiyat": toasosayısı * float(toasofiyat),
    "Toplam Kar": (float(toasofiyat) - toaso_alış_ort) * toasosayısı,
    "Yüzdelik Kar Oranı" : (toaso_Kar/float(toasofiyat)) * 100
}
df12 = pandas.DataFrame([new_row12])

#KÜÇÜK TOPLAMA İŞLEMŞLERİ
rows = [new_row1,new_row2,new_row3,new_row4,new_row5,new_row6,new_row7,new_row8,new_row9,new_row10,new_row11,new_row12]
toplamkar = 0
toplamgüncelfiyat = 0
for new_row in rows:
    toplamkar += new_row["Toplam Kar"]
    toplamgüncelfiyat += new_row["Güncel Toplam Fiyat"]

#TOPLAMLARI YAZDIR[EN ALTTA OLMA SEBEBİ }361{ ]
new_row_toplam = {
    "Hisse" : "Toplamlar >> >> >> ",
    "Toplam Kar" : toplamkar,
    "Yüzdelik Kar Oranı" : ( toplamkar / toplamgüncelfiyat ) * 100,
    "Güncel Toplam Fiyat" :toplamgüncelfiyat
}
dftoplam = pandas.DataFrame([new_row_toplam])

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def renklendirme(val):
    color = 'red' if val < 0 else 'green'
    return 'color: {}'.format(color)

dataframes = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12,dftoplam]
tüm_datalar = pandas.concat(dataframes)
tüm_datalar.reset_index(drop=True,inplace=True)
tüm_datalar_styed = tüm_datalar.style.applymap(renklendirme, subset=["Yüzdelik Kar Oranı","Toplam Kar"])
#OLŞACAK DOSYAIN ADINI BELİRLEME
while True: 
    DosyaAdı = input("OLUŞACAK DOSYAININ ADINI BELİRLE: ")
    if "\\ " in DosyaAdı or "/ " in DosyaAdı or ":" in DosyaAdı or  "*" in DosyaAdı or "<" in DosyaAdı or ">" in DosyaAdı :
        print('GEÇERSİZ Toplam KarAKTERLERİ KULLANMA! (   \  /  :  *  ?  "  <  >   )')
    else: 
        break

# Excel dosyasına yaz
tüm_datalar_styed.to_excel("D:/Düzenli Masaüstü Remote/Excel & Borsa.py/ciktilar/{}.xlsx".format(DosyaAdı), index=False)

print("OLUŞAN DOSYAYI BU ADRESTEN BULABİLİRSİN: D:/Düzenli Masaüstü Remote/Excel & Borsa.py/ciktilar/{}.xlsx".format(DosyaAdı))

#TO DO:       Güncel Toplam Fiyat Toplam KarLARI TOPLAYIP EXCELDE YENİ BİR ROW'DA YAZAN KOMUT YAZ!! +++ tamamlandı +++
