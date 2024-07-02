#1.soru
#T1
pay=[15,-5,3,-2]
payda=[10,8,15,9]
toplam=0
for x in range (0,4):
    toplam=pay[x]/payda[x]+toplam
    
print(toplam)

#T2
t=0
pay=1
payda=5
for x in range (0,4):
         t=t+ pay/payda
         pay = pay*5
         payda = payda*5
print(t)

print('\n*************\n')
#T2
pay = [1,5,25,-125]
payda=[5,25,125,625]
toplam=0
for x in range(0,4):
    toplam=pay[x]/payda[x]+toplam
print(toplam)


print('\n**************\n')
#T2
pay=[1,5,25,-125]
payda=[5,25,125,625]
toplam=0
for x in range(0,4):
    toplam=pay[x]/payda[x]+toplam
print(toplam)

print('\n-------------\n')
#2.soru
şehir=["antalya"]
mahalle=["ıhlamurkuyu mahallesi"]
sokak=["akdeniz sokak"]
print(mahalle[0]+sokak[0]+şehir[0])