def ask():
    try:
        kom = int(input('''
    Yapabileceğiniz işlemler:
    1. Not Ekle
    2. Not Güncelle
    3. Not Sil
    4. Notları Listele
    5. Çıkış
    Lütfen bir işlem seçin (1/2/3/4/5): '''))
        print('')
        return kom
    except ValueError:
        print('SAYI GİR DENYOO')
notlar_listesi = {}
while True:
    komut = ask()
    if komut == 1:
        title = input('Not başlığını girin: ')
        if title in notlar_listesi:
            print('Not zaten eklidir lo')
            continue
        content = input('Not içeriğini girin: ')
        if title not in notlar_listesi:
            notlar_listesi[title] = [content]
            print(f'Not eklendi: {content}')

    elif komut == 2:
        tobeupdated = input('Güncellenecek notun başlığını girin: ')
        if tobeupdated in notlar_listesi:
            new_content = input('Yeni içeriği gir: ')
            notlar_listesi[tobeupdated] = new_content
        else:
            print('yooo ')
            continue

    elif komut == 3:
        tobedeleted = input('Silmek istediğin notun başlığı: ')
        if tobedeleted in notlar_listesi:
            notlar_listesi.pop(tobedeleted)
            print(f'{tobedeleted} başlıklı not silindi. ')
        else:
            print('Öyle bir şey yook. ')

    elif komut == 4:
        print(notlar_listesi)

    elif komut == 5:
        exit()