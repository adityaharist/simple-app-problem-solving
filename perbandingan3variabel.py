def intro():
 print("Program ini akan menentukan seberapa jauh jarak tempuh")
 print("apabila jumlah bensin diketahui, dan sebaliknya\n")

def ketentuanPadaJarak():
 ketentuanJarak = 60
 ketentuanBensin = 1
 return ketentuanJarak / ketentuanBensin

def ketentuanPadaBensin():
 ketentuanJarak = 60
 return ketentuanJarak
 
def hitungBensin():
 jarak = float(inputanBensin())
 if jarak <= 0:
  errorInputan()
   
 syarat = float(ketentuanPadaBensin())
 bensin = jarak / syarat
 
 jarak = int(jarak)
 
 print("Jika anda menempuh jarak sejauh %d Km, maka anda membutuhkan bensin sebanyak %.2f Liter." % (jarak, bensin))
 print("")
 print("")
 tanya()
  
def inputanBensin():
 jarak = input("Masukkan jarak yang ditempuh : ")
 jarak = int(jarak)
 
 return jarak

def hitungJarak():
 bensin = inputanJarak()
 if bensin <= 0 or bensin >= 50:
  errorInputan()
  
 syarat = ketentuanPadaJarak()
 jarak = bensin * syarat
 
 print("Dengan jumlah bensin sebanyak",bensin,"Liter,Anda dapat menempuh jarak sejauh",jarak,"Km.")
 print("")
 print("")
 tanya()
   
def inputanJarak():
 bensin = input("Masukkan jumlah bensin : ")
 bensin = int(bensin)
 
 return bensin

def ketemuJarak():
 bensin = inputJarak()
 jarak = hitungJarak()

def tanya():
 mauLagi = input("Hitung Lagi ? (y/n) : ")
 if mauLagi.lower() == 'y':
  mainlagi()
 else:
  print("Selamat tinggal! :) ")
  exit()
  
def errorInputan():
 print("Inputan tidak valid bro")
 mainlagi()

def mainlagi():
 intro() 
 tanya = input("Hitung Jarak atau Bensin ? (jarak/bensin): ")
 
 if tanya.lower() == 'jarak':
  hitungJarak()
  
 elif tanya.lower() == 'bensin':
  hitungBensin()
  
 else:
  errorInputan()
  
mainlagi()