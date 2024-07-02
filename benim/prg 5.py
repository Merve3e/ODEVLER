import math # karekök ve diğer fonksiyonlar için
# girilen sayı pozitif/negatif mi?
sayi = int(input('İlk Sayıyı girin : '))

#if (int(sayi)>0):
if (sayi>0):
    print(sayi,"pozitif")
else:
    if(sayi ==0):
        print (sayi,"sıfır")
    else:
        print (sayi,"negatif")
    
#girilen sayı tek/çift mi?
sayi = input('ikinci sayıyı girin : ')

if(int(sayi) %2 == 0):
    print(int(sayi),"çift")
else:
    print(int(sayi),"tek")
    
#girilen sayının karekökü tamsayı mı?
sayi = input('karekökü alınacak sayıyı girin :')
n=math.sqrt(float(sayi));
if (float(n*n) == int(sayi)):
#if (float(n*n)==int(sayi)):
#  sayi=8 ise n=2.82 ==>2.82*2.82=7.95 karşılaştur 8==>(7.95 ==8)    
    print(sayi,"sayısının karekoku bir tamsayidir.",n);
else:
    print(sayi,"sayısının karekoku bir tamsayi değildir.",n);
        
#girilen sayı 0 ile 100 aralığında mı
sayi=input('0 ile 100 arası bir sayıyı girin:')
if(int(sayi)>=0):
    if(int(sayi)<=100):
        print(sayi,"sayısı [0 100] aralığındadır")
    else:
        print(sayi,"100'den büyüktür.")
        
else:
    print(sayi,"0'dan küçüktür.")
    
    
#girilen 2 sayıdan hangisi diğerinden büyük veya eşit mi?
sayi1=input('ilk sayıyı girin : ')
sayi2=input('ikinci sayıyı girin : ')
    
if(int(sayi1) >int(sayi2)):
   print(sayi1,sayi2,"den büyük")
else:
    if(int(sayi1)< int(sayi2)):
       print(sayi2,sayi1,"den büyük")
    else:
       print("sayılar eşit.")
    