while(True ):
    result = input("Hangi işlemi yapmak istiyorsunuz : + - * / veya Çıkış için C'ye basınız : ")
    if(result == "C"):
        break
    if (result =="+"):
        first_number = input("Birinci sayıyı giriniz: ")
        second_number = input("İkinci sayıyı giriniz: ")
        print("Toplama: ", int(first_number) + int(second_number))
    elif (result =="-"):
        first_number = input("Birinci sayıyı giriniz: ")
        second_number = input("İkinci sayıyı giriniz: ")
        print("Çıkarma: ", int(first_number) - int(second_number))
    elif (result =="*"):
        first_number = input("Birinci sayıyı giriniz: ")
        second_number = input("İkinci sayıyı giriniz: ")
        print("Çarpma: ", int(first_number) * int(second_number))
    elif (result =="/"):
        first_number = input("Birinci sayıyı giriniz: ")
        second_number = input("İkinci sayıyı giriniz: ")
        print("Bölme: ", int(first_number) / int(second_number))