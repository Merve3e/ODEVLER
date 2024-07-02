#1.ödev
sayi=input('-10 ile 10 arası bir sayıyı girin:')
if(int(sayi)>=-10):
    if(int(sayi)<=10):
        print(sayi,"sayısı [-10 10] aralığındadır")
    else:
        print(sayi,"10'dan büyüktür.")
        
else:
    print(sayi,"-10'dan küçüktür.")
    
#2.ödev    
sayi1=input('doğum tarihini girin : ')
if(int(sayi1) >2004):
   print("18 yasından küçük")
if(int(sayi1)==2004):
    print("18 yasındadır")
else:
    if(int(sayi1)< 2004):
       print("18 yasından büyük")
       
#3.ödev      
a = input("ilk sayı girin: ")
b = input("ikinci sayıyı girin: ")
c = input("üçüncü sayıyı girin: ")
if ((a==b) !=c) and ((a==c) !=b) and ((b==c) !=a):
    print("ikizkenar")
else:
    print("ikizkenar degildir")
   
