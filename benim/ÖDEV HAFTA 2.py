print("basınç formülü")

G=float(input("Cismin ağırlığı:"))
A=float(input("yüzey alanı:"))
P= G/A
print("katı basıncı="+str(P))

print("Güç formülü")

W=float(input("İş:"))
t=float(input("toplam geçen süre:"))
P= W/t
print("Güç="+str(P))

print("ısı formülü")

m=float(input("Kütlesi:"))
c=float(input("Özısısı:"))
Δt=float(input("Sıcaklık farkı:"))
Q=m*c*Δt
print("Isi="+str(Q))