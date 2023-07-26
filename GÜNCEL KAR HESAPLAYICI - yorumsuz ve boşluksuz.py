import os
import openpyxl 
import pandas
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
maddeler = ["Hisse","Hisse sayısı", "Alış Fiyatı(ort.)","Güncel satış fiyatı", "Toplam Kar","Güncel Toplam Fiyat","Yüzdelik Kar Oranı"]
df = pandas.DataFrame(columns=maddeler)
df
edge_options = Options()
edge_options.add_argument("--incognito")
edge_options.add_argument("--headless")
driver = webdriver.Edge(options=edge_options)
driver.delete_all_cookies()
max_attempts = 5
attempts = 0
while attempts < max_attempts:
    driver.get("https://www.foreks.com/sembol-detay/H2024/froto/ford-otosan")
    driver.implicitly_wait(40)
    try:
        frotofiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        frotofiyat = frotofiyat_element.text.strip().replace(",", ".")
        frotofiyat = float(frotofiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://www.foreks.com/sembol-detay/H1946/bimas/bim-magazalar")
    driver.implicitly_wait(40)
    try:
        bimasfiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        bimasfiyat = bimasfiyat_element.text.strip().replace(",", ".")
        bimasfiyat = float(bimasfiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://www.foreks.com/sembol-detay/H2122/tuprs/tupras")
    driver.implicitly_wait(40)
    try:
        tuprsfiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        tuprsfiyat = tuprsfiyat_element.text.strip().replace(",", ".")
        tuprsfiyat = float(tuprsfiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://www.foreks.com/sembol-detay/H2892/aksa/aksa")
    driver.implicitly_wait(40)
    try:
        aksafiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        aksafiyat = aksafiyat_element.text.strip().replace(",", ".")
        aksafiyat = float(aksafiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://www.foreks.com/sembol-detay/H2126/kords/kordsa-teknik-tekstil")
    driver.implicitly_wait(40)
    try:
        kordsfiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        kordsfiyat = kordsfiyat_element.text.strip().replace(",", ".")
        kordsfiyat = float(kordsfiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://www.foreks.com/sembol-detay/H2674/eregl/eregli-demir-celik")
    driver.implicitly_wait(40)
    try:
        ereglfiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        ereglfiyat = ereglfiyat_element.text.strip().replace(",", ".")
        ereglfiyat = float(ereglfiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://www.foreks.com/sembol-detay/H1461005/astor/astor-enerji")
    driver.implicitly_wait(40)
    try:
        astorfiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        astorfiyat = astorfiyat_element.text.strip().replace(",", ".")
        astorfiyat = float(astorfiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://www.foreks.com/sembol-detay/H830949/bioen/biotrend-cevre-ve-enerji")
    driver.implicitly_wait(40)
    try:
        bioenfiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        bioenfiyat = bioenfiyat_element.text.strip().replace(",", ".")
        bioenfiyat = float(bioenfiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://www.foreks.com/sembol-detay/H1452897/soke/soke-degirmencilik")
    driver.implicitly_wait(40)
    try:
        sokefiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        sokefiyat = sokefiyat_element.text.strip().replace(",", ".")
        sokefiyat = float(sokefiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://www.foreks.com/sembol-detay/H2888/vesbe/vestel-beyaz-esya")
    driver.implicitly_wait(40)
    try:
        vesbefiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        vesbefiyat = vesbefiyat_element.text.strip().replace(",", ".")
        vesbefiyat = float(vesbefiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://foreks.com/sembol-detay/H1388185/ALFAS/alfa-solar-enerji")
    driver.implicitly_wait(40)
    try:
        alfasfiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        alfasfiyat = alfasfiyat_element.text.strip().replace(",", ".")
        alfasfiyat = float(alfasfiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
while attempts < max_attempts:
    driver.get("https://foreks.com/sembol-detay/H2108/toaso/tofas-oto-fab")
    driver.implicitly_wait(40)
    try:
        toasofiyat_element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/strong')
        toasofiyat = toasofiyat_element.text.strip().replace(",", ".")
        toasofiyat = float(toasofiyat)
        break
    except ValueError:
        print("Hata: Veri boş veya geçersiz. Tekrar denetleniyor...")
        attempts += 1
    except Exception as e:
        print("Hata:", e)
        attempts += 1
froto_Kar = float(frotofiyat) -  572.90
new_row1 = {
    "Hisse": "FROTO",
    "Hisse sayısı" : 1,
    "Alış Fiyatı(ort.)": 572.90,
    "Güncel satış fiyatı": frotofiyat,
    "Güncel Toplam Fiyat": 1 * float(frotofiyat),
    "Toplam Kar": (float(frotofiyat) - 572.90) * 1,
    "Yüzdelik Kar Oranı" : (froto_Kar/float(frotofiyat)) * 100
}
df1 = pandas.DataFrame([new_row1])
bimas_Kar = float(bimasfiyat) - 174.60
new_row2 = {
    "Hisse": "BİMAS",
    "Hisse sayısı" : 1,
    "Alış Fiyatı(ort.)": 174.60,
    "Güncel satış fiyatı": bimasfiyat,
    "Güncel Toplam Fiyat": 1 * float(bimasfiyat),
    "Toplam Kar": (float(bimasfiyat) - 174.60)*1,
    "Yüzdelik Kar Oranı" : (bimas_Kar/float(bimasfiyat)) * 100
}
df2 = pandas.DataFrame([new_row2])
tuprs_Kar = float(tuprsfiyat) - 73.8
new_row3 = {
    "Hisse": "TUPRS",
    "Hisse sayısı" : 3,
    "Alış Fiyatı(ort.)": 73.8,
    "Güncel satış fiyatı": tuprsfiyat,
    "Güncel Toplam Fiyat": 3 * float(tuprsfiyat),
    "Toplam Kar": (float(tuprsfiyat) - 73.8 ) * 3,
    "Yüzdelik Kar Oranı" : (tuprs_Kar/float(tuprsfiyat)) * 100
}
df3 = pandas.DataFrame([new_row3])
aksa_Kar = float(aksafiyat) - 68.59
new_row4 = {
    "Hisse": "AKSA",
    "Hisse sayısı" : 7,
    "Alış Fiyatı(ort.)": 68.59,
    "Güncel satış fiyatı": aksafiyat,
    "Güncel Toplam Fiyat": 7 * float(aksafiyat),
    "Toplam Kar": (float(aksafiyat) - 68.59) * 7,
    "Yüzdelik Kar Oranı" : (aksa_Kar/float(aksafiyat)) * 100
}
df4 = pandas.DataFrame([new_row4])
kords_Kar = float(kordsfiyat) - 63.15
new_row5 = {
    "Hisse": "KORDS",
    "Hisse sayısı" : 1,
    "Alış Fiyatı(ort.)": 63.15,
    "Güncel satış fiyatı": kordsfiyat,
    "Güncel Toplam Fiyat": 1 * float(kordsfiyat),
    "Toplam Kar": (float(kordsfiyat) - 63.15) * 1,
    "Yüzdelik Kar Oranı" : (kords_Kar/float(kordsfiyat)) * 100
}
df5 = pandas.DataFrame([new_row5])
eregl_Kar = float(ereglfiyat) - 33.24
new_row6 = {
    "Hisse": "EREGL",
    "Hisse sayısı" : 10 ,
    "Alış Fiyatı(ort.)": 33.24 ,
    "Güncel satış fiyatı": ereglfiyat,
    "Güncel Toplam Fiyat": 10 * float(ereglfiyat),
    "Toplam Kar": (float(ereglfiyat) - 33.24 ) * 10,
    "Yüzdelik Kar Oranı" : (eregl_Kar/float(ereglfiyat)) * 100
}
df6 = pandas.DataFrame([new_row6])
astor_Kar = float(astorfiyat) - 24.72
new_row7 = {
    "Hisse": "ASTOR",
    "Hisse sayısı" : 1 ,
    "Alış Fiyatı(ort.)": 24.72,
    "Güncel satış fiyatı": astorfiyat,
    "Güncel Toplam Fiyat": 1 * float(astorfiyat),
    "Toplam Kar": (float(astorfiyat) - 24.72) * 1,
    "Yüzdelik Kar Oranı" : (astor_Kar/float(astorfiyat)) * 100
}
df7 = pandas.DataFrame([new_row7])
bioen_Kar = float(bioenfiyat) - 13.88
new_row8 = {
    "Hisse": "BİOEN",
    "Hisse sayısı" : 8,
    "Alış Fiyatı(ort.)": 13.88,
    "Güncel satış fiyatı": bioenfiyat,
    "Güncel Toplam Fiyat": 8 * float(bioenfiyat),
    "Toplam Kar": (float(bioenfiyat) - 13.88 ) * 8,
    "Yüzdelik Kar Oranı" : (bioen_Kar/float(bioenfiyat)) * 100
}
df8 = pandas.DataFrame([new_row8]) 
soke_Kar = float(sokefiyat) - 12.05
new_row9 = {
    "Hisse": "SOKE",
    "Hisse sayısı" : 6,
    "Alış Fiyatı(ort.)": 12.05 ,
    "Güncel satış fiyatı": sokefiyat,
    "Güncel Toplam Fiyat": 6 * float(sokefiyat),
    "Toplam Kar": (float(sokefiyat) - 12.05 ) * 6,
    "Yüzdelik Kar Oranı" : (soke_Kar/float(sokefiyat)) * 100
}
df9 = pandas.DataFrame([new_row9])
vesbe_Kar = float(vesbefiyat) - 10.28
new_row10 = {
    "Hisse": "VESBE",
    "Hisse sayısı" : 10 ,
    "Alış Fiyatı(ort.)": 10.28,
    "Güncel satış fiyatı": vesbefiyat,
    "Güncel Toplam Fiyat": 10 * float(vesbefiyat),
    "Toplam Kar": (float(vesbefiyat) - 10.28) * 10,
    "Yüzdelik Kar Oranı" : (vesbe_Kar/float(vesbefiyat)) * 100
}
df10 = pandas.DataFrame([new_row10])
alfas_Kar = float(alfasfiyat) - 444.60
new_row11 = {
    "Hisse": "ALFAS",
    "Hisse sayısı" : 1 ,
    "Alış Fiyatı(ort.)": 444.60,
    "Güncel satış fiyatı": alfasfiyat,
    "Güncel Toplam Fiyat": 1 * float(alfasfiyat),
    "Toplam Kar": (float(alfasfiyat) - 444.60) * 1,
    "Yüzdelik Kar Oranı" : (alfas_Kar/float(alfasfiyat)) * 100
}
df11 = pandas.DataFrame([new_row11])
toaso_Kar = float(toasofiyat) - 241.90
new_row12 = {
    "Hisse": "TOASO",
    "Hisse sayısı" : 2 ,
    "Alış Fiyatı(ort.)": 241.90,
    "Güncel satış fiyatı": toasofiyat,
    "Güncel Toplam Fiyat": 2 * float(toasofiyat),
    "Toplam Kar": (float(toasofiyat) - 241.90) * 2,
    "Yüzdelik Kar Oranı" : (toaso_Kar/float(toasofiyat)) * 100
}
df12 = pandas.DataFrame([new_row12])
rows = [new_row1,new_row2,new_row3,new_row4,new_row5,new_row6,new_row7,new_row8,new_row9,new_row10,new_row11,new_row12]
toplamkar = 0
toplamgüncelfiyat = 0
for new_row in rows:
    toplamkar += new_row["Toplam Kar"]
    toplamgüncelfiyat += new_row["Güncel Toplam Fiyat"]
new_row_toplam = {
    "Hisse" : "Toplamlar >> >> >> ",
    "Toplam Kar" : toplamkar,
    "Yüzdelik Kar Oranı" : ( toplamkar / toplamgüncelfiyat ) * 100,
    "Güncel Toplam Fiyat" :toplamgüncelfiyat
}
dftoplam = pandas.DataFrame([new_row_toplam])
def renklendirme(val):
    color = 'red' if val < 0 else 'green'
    return 'color: {}'.format(color)

dataframes = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12,dftoplam] 
tüm_datalar = pandas.concat(dataframes)
tüm_datalar.reset_index(drop=True,inplace=True)
tüm_datalar_styed = tüm_datalar.style.applymap(renklendirme, subset=["Yüzdelik Kar Oranı","Toplam Kar"])
while True: 
    DosyaAdı = input("OLUŞACAK DOSYAININ ADINI BELİRLE: ")
    if "\\ " in DosyaAdı or "/ " in DosyaAdı or ":" in DosyaAdı or  "*" in DosyaAdı or "<" in DosyaAdı or ">" in DosyaAdı :
        print('GEÇERSİZ Toplam KarAKTERLERİ KULLANMA! (   \  /  :  *  ?  "  <  >   )')
    else: 
        break
kullanici_klasor = os.path.expanduser("~")
dosya_dizini = os.path.join(kullanici_klasor, "OneDrive", "Masaüstü", "SELENIUM OUTPUTS")
if not os.path.exists(dosya_dizini):
    os.makedirs(dosya_dizini)
tüm_datalar_styed.to_excel(os.path.join(dosya_dizini, "{}.xlsx".format(DosyaAdı)), index=False)
print("OLUŞAN DOSYAYI BU ADRESTEN BULABİLİRSİN: {}".format(os.path.join(dosya_dizini, "{}.xlsx".format(DosyaAdı))))