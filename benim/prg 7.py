#döngüler 

for num in range(5,8):
    print(num)
    
for x in range(6):
    print(x)
    
for x in range(2,30,3):
    print(x)
#for bittikten sonra istediğin şeyi else ile yapmaca
else:
    print("son")
#döngüden çıkmak için BREAK komutu
for x in range(10):
    if x==4:break
    print(x)
else:    #break olunca else çalışmaz
    print("son")
#dizi(sıralı şeyler)veriyosak köşeli parantez olmalı   
for x in [10,443,11,12]:
    print(x)
for harf in 'python':
    print('harfleri listele:',harf)
for harf in 'merv37*!':
    print('harfleri listele:',harf)
#listeyi farklı kullanım    
meyveler = ['banana','apple','mango']
for meyve in meyveler:
    print('meyve listele:',meyve)
 
meyveler=['banana','apple','mango']
for index in range(len(meyveler)):
    print('meyve listele:',meyveler[index])
#WHİLE(içinde sayaç yok koşul var ama sayaçta içerebilir)range yok
i=1
while i<6:
    print(i)
    i += 1

i=15
while i<=20:
    print(i)
    i +=1
#iç içe döngüler
#range koymıcaz ki alttaki örnekte 6 olmasın
for x in(5,7):
    for y in(1,2):
        print(x,y)
        
for num in range(4,7):
    for i in range(2,num):
        print(num,' ',i)


for x in range(1,6):
    print('\n')
    for y in range(0,x):
        print(x,end=' ')
    
a=10
print(a,'sayısının tam bölenleri')

for i in range(1, a+1):
    if ((a % i)==0):
        print(i,'ile tam bölünür')
    

        

    

