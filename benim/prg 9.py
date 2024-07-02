#matrisler
a = ([[11,12,13,14],
      [15,16,17,18],
      [19,20,21,22]])
#tüm matris
print("matrisin yazdırılması\n",a)

print("\nmatrisin formatlı yazdırılması\n",a)
for satir in range(0,3):
    for sutun in range(0,4):
        print (satir,sutun,' satir-sutun ',a[satir][sutun])
    print('\n')
    
print("\nmatrisin 1.satır,2.sütunu",a[0][1])

print('\n****************\n')
print("matrisin toplamı")
t=0
for satir in range(0,3):
    for sutun in range(0,4):
        t=t+a[satir][sutun]
print('\n matris toplamı=',t)

print('\n**********?n')
t=0
for sutun in range(0,4):
    t=t+a[1][sutun]
print('\n matris 2.satırının toplamı=',t)