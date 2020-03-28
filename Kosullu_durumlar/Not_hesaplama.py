print("hoş geldiniz not similasyonu başlatılıyor..")

vize1 = int(input("Lütfen ilk vizeden aldığınız notu giriniz:"))
vize2 = int(input("Lütfen ikinci vizeden aldığınız notu giriniz: "))
final = int(input("Lütfen finalden aldığınız notu giriniz: "))

vize1 = vize1 * 3/10
vize2 = vize2 * 3/10
final = final * 4/10

not_ortalaması = float(vize1+vize2+final)

if not_ortalaması >= 90:
    print("notun {} AA Tebrikler geçtiniz".format(not_ortalaması))
elif not_ortalaması >= 85:
    print("notun {} BA Tebrikler geçtiniz".format(not_ortalaması))
elif not_ortalaması >= 80:
    print("notun {} BB Tebrikler geçtiniz".format(not_ortalaması))
elif not_ortalaması >= 75:
    print("notun {} CA Tebrikler geçtiniz".format(not_ortalaması))
elif not_ortalaması >= 70:
    print("notun {} CB Tebrikler geçtiniz".format(not_ortalaması))
elif not_ortalaması >= 65:
    print("notun {} DA Tebrikler geçtiniz".format(not_ortalaması))
elif not_ortalaması >= 60:
    print("notun {} DB Tebrikler geçtiniz".format(not_ortalaması))
elif not_ortalaması >= 55:
    print("notun {} FD sorunlu geçtin".format(not_ortalaması))
else:
    print("notun {} FF üzgünüm kaldın".format(not_ortalaması))