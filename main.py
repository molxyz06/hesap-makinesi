ilksayi = int(input("Ilk Sayinizi Giriniz: "))
ikincisayi = int(input("Ikinci Sayinizi Giriniz: "))
islem = str(input("""Yapmak Istediginiz Islemi Giriniz
(Toplama: +, Cikarma: -, Carpma: x, Bolme: /) """))



if islem == "+":
    print(ilksayi + ikincisayi)

elif islem == "-":
    print(ilksayi - ikincisayi)

elif islem == "x":
    print(ilksayi * ikincisayi)

elif islem == "/":
    print(int(ilksayi / ikincisayi))

else:
    print("Isleminiz algilanamadi, lutfen tekrar deneyiniz.")

