print('Haftanın günlerini sayıyla sorunuz.')
print('mesela salı saat 15:00i sormak için önce 2 sonra 15 yaz')
if int(input('Hangi günleri soruyon')) in range(1, 6):
    if int(input('Hangi saatler arası')) in range(10, 21):
        print('açık')
    else:
        print('kapalı')
else:
    print("kapalı")
#kodu kibarlaştırmaya üşendim