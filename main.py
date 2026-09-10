while True:
    ilksayi = int(input("Ilk Sayinizi Giriniz: "))
    ikincisayi = int(input("Ikinci Sayinizi Giriniz: "))
    islem = str(input("""Yapmak Istediginiz Islemi Giriniz
(Toplama: +, Cikarma: -, Carpma: x, Bolme: /) """))


    if islem == "+":
        print("Sonuc: " + str(ilksayi + ikincisayi))

        tekrarislem = input("Tekrar Islem Yapmak Ister Misiniz?(evet: e, hayir: h)")
        if tekrarislem == "e":
            continue
        else:
            break

    elif islem == "-":
        print("Sonuc: " + str(ilksayi - ikincisayi))

        tekrarislem = input("Tekrar Islem Yapmak Ister Misiniz?(evet: e, hayir: h)")
        if tekrarislem == "e":
            continue
        else:
            break

    elif islem == "x":
        print("Sonuc: " + str(ilksayi * ikincisayi))

        tekrarislem = input("Tekrar Islem Yapmak Ister Misiniz?(evet: e, hayir: h)")
        if tekrarislem == "e":
            continue
        else:
            break

    elif islem == "/":
        print("Sonuc: " + str(int(ilksayi / ikincisayi)))

        tekrarislem = input("Tekrar Islem Yapmak Ister Misiniz?(evet: e, hayir: h)")
        if tekrarislem == "e":
            continue
        else:
            break

    else:
        print("Isleminiz algilanamadi, lutfen tekrar deneyiniz.")
        continue

