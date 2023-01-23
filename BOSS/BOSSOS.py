# BOSS İşletim Sistemi Projesi
import enum
import os
import random
import sys
from time import sleep
from venv import create


def SplashScreen():
    print("BOSS SYSTEM")
    print("")
    print("BOSS İşletim Sistemine Hoşgeldiniz!")
    print("Lütfen bekleyiniz!")
    createStar(20)


# işletim sistemininden çıkış methodu
def ExitOS():
    print("")
    print("İşletim Sisteminden çıkışınız yapılıyor...")
    print("Lütfen bekleyiniz.")
    createStar(20)






# def DosyaKapat():
#     file_object.close()

# def DosyaSil():
    
#     if os.path.isfile('C:/Desktop/OSDeneme/sample.txt'):
#         os.remove('C:/Desktop/OSDeneme/sample.txt'):
#         print("Done")
#     else:
#         print('The file doesnt exist')

# def VeriEkle():
#     f = open(":\Users\Batuhan\Desktop\OSDeneme", "a")
#     f.write("Artık dosyada daha çok veri var!")
#     f.close()




# İşletim sisteminde görsel amaçlı kullanılan yıldızlar
def createStar(numberofStars):
    line = "*"
    for i in range(numberofStars):
        print(line, end=" ")
        sleep(1)


# Süreçleri tutan Enum Class Kısmı
class Loglevel(enum.Enum):
    def StartProcess():
        return "Süreciniz başlatılıyor"

    def SystemCall():
        return "Sistem çağrınız yapılıyor"

    def StopProcess():
        return "Süreciniz sonlandırılıyor"

    def TimerInterrupt():
        return "Zamanlayıcı kesimi"


#Çizelgeleme Algoritmamızın Fonksiyonlarını Kodladığımız Kısım

def ScheduleAlgorithm(n):
    
    
    
    print("Mevcut süreç sayısı: ",n);
    d = dict()
     
   
    
    for i in range(n):
        key = "P: "+str(liste[i]())
        a = int(input(str(liste[i]())+" için başlangıç zamanını giriniz: "))
        b = int(input(str(liste[i]())+" için çalışma süresi giriniz: "))
        l = []
        l.append(a)
        l.append(b)
        d[key] = l
     
    d = sorted(d.items(), key=lambda item: item[1][0])
     
    ET = []
    for i in range(len(d)):
        # İlk Sürecimiz
        if(i==0):
            ET.append(d[i][1][1])
     
        
        else:
            ET.append(ET[i-1] + d[i][1][1])
     
    TAT = []
    for i in range(len(d)):
        TAT.append(ET[i] - d[i][1][0])
     
    WT = []
    for i in range(len(d)):
        WT.append(TAT[i] - d[i][1][1])
     
    avg_WT = 0
    for i in WT:
        avg_WT +=i
    avg_WT = (avg_WT/n)
     
    print("Sürecler                   | Baslangic | Calisma | Cikis | Turn Around | Bekleme |")
    
    osdosya1 = open("OSDosyamiz.txt", "w") 
    osdosya1.write("Sürecler                   | Baslangic | Calisma | Cikis | Turn Around | Bekleme  |\n")
    
    for i in range(n):
          print("",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
          
          #Sürecimizden,olusturdugumuz dosyaya yazdırma kısmı:
          osdosya1.write("***");
          osdosya1.write(str(d[i][0]));
          osdosya1.write("   /   ")
          osdosya1.write(str(d[i][1][0]))
          osdosya1.write("   /         ")
          osdosya1.write(str(d[i][1][1]))
          osdosya1.write("   /   ")
          osdosya1.write(str(ET[i]))
          osdosya1.write("    /    ")
          osdosya1.write(str(TAT[i]))
          osdosya1.write("  /  ")
          osdosya1.write(str(WT[i]))
          osdosya1.write("   /         ")
          osdosya1.write("\n")
         
            #Kullanıcıya haber verme kısımları
    print("Ortalama Bekleme Süresi: ",avg_WT)  #Bekleme Süresini bildirdiğimiz kısım
    print("Veriler Arsivleniyor.")
    sleep(2)
    print("Veriler Arsivlendi.")
    sleep(1)

 
   



   # MAIN KISMI #


# Processlerimizi içeren listemiz.

liste=[Loglevel.StartProcess, Loglevel.SystemCall, Loglevel.StopProcess, Loglevel.TimerInterrupt]

listeBoyutu = len(liste)

ScheduleAlgorithm(listeBoyutu)


kalan = []

print("****")

print("Listemizin Adresi: ", hex(id(liste))) 


#Sayaç Kısmı
counter = 0
while counter<=3:
    
    
    
    print(liste[counter](), "Decimal : "  ,(id(liste[counter])))

    # Logical Adresin son 5 hanesini tutuyoruz.

    kalan.append(id(liste[counter]) % 100000) 
    
    
    liste[counter]()
    
    #Döngü bitirici sayacımızı arttırıyoruz.
    counter = counter+1


print("***")




counter = 0
while counter <= 3:
    sayi = id(kalan[counter])

    binarySayi = " "
    
    while sayi!=0:

        binarySayi = str(sayi%2)+binarySayi

        sayi = sayi//2
    

    print(binarySayi)
        

    counter += 1


# Rastgele olusturdugumuz sayfa tablosu dizisi:

page = [17, 34, 1, 9, 87, 21, 27, 17, 33, 7, 3, 0 , 4, 23, 25,11,20,2,1,16,3,6,4,7,2,4,11,19,15,6,7,2,4,6] 





print("\n **** SAYFALAMA HESAPLAYICISI **** \n")


#Sayaç Kısmı

counter =0

while counter <=3:
    

    # İstenen Girdiler Kısmı

    kb = 4
    sanal_adres = kalan[counter]
    
    page_kd = (kb * 1024)
    virtual_page_number = (int(sanal_adres) / page_kd)
    offset = (int(sanal_adres) % page_kd)
    
    pageFrame=page[int(virtual_page_number)]
    sayfaAdresi=(page_kd*pageFrame)-1
    fizikselAdres=sayfaAdresi+offset
    
    # Kullanıcıya gösterilen kısımlar
    print("\n ##### İşlemler ##### \n")
    
    print(" Hatırlatma Notu: 1kb = 1024\n")
    print(" Boyut: "+str(kb)+"KB ve sanal adres - "+str(sanal_adres))
    print(" "+str(sanal_adres)+"/"+str(kb)+"k")
    print(" "+str(sanal_adres)+"/"+str(page_kd)+" = "+str(int(virtual_page_number))+" rem "+str(offset))
    
    # Sonucların Gosterildigi Kısım

    print("\n **** SONUCLAR **** \n")
    print(" Sanal sayfa numarası = " + str(int(virtual_page_number)))
    print(" Offset = " + str(offset))
    
    print("Sayfa Çerçevesi: ", str(pageFrame))
    print("Sayfa Adresi: ", str(sayfaAdresi))
    
    
    print("****")
    
    counter+=1





# Sistemden çıkış methodumuz
ExitOS()