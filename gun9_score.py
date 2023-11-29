if __name__ == '__main__':
    isim_skor = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        isim_skor.append([name, score])
    isim_skor.sort(key=lambda x: (x[1], x[0]))
    düşükskor = sorted(set([s[1] for s in isim_skor]))[1]
    for name, puan in isim_skor:
        if puan == düşükskor:
           print(name)