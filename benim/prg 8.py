#a üssü b
def UsAl(sayi,us):
    sonuc=1
    for i in range(us):
        sonuc=sonuc*sayi
    return sonuc
 
s1=int(input('Sayıyı Gir : '))
s2=int(input('Üs Gir : '))
print (UsAl(s1,s2))
 


#n!
sayi = int(input("Faktöriyelini Hesaplamak için sayı giriniz:"))
deger = 1
for i in range(sayi):
    deger = deger * (i+1)
 
print("Faktoriyel : ", deger)