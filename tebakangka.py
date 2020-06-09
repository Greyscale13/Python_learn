import random

a = (random.randrange(1, 10))
tebak = int(input("Coba tebak angka dari 1 sampai 9: "))
while True:
    if tebak == a-1:
        print("Antara kurang satu atau kelebihan satu, coba lagi")
        tebak = int(input("Coba tebak angka dari 1 sampai 9: "))
    elif tebak == a+1:
        print("Antara kurang satu atau kelebihan satu, coba lagi")
        tebak = int(input("Coba tebak angka dari 1 sampai 9: "))
    elif tebak > a+1:
        print("Kegedean masih, coba lagi")
        tebak = int(input("Coba tebak angka dari 1 sampai 9: "))
    elif tebak < a-1:
        print("Kekecilan masih, coba lagi")
        tebak = int(input("Coba tebak angka dari 1 sampai 9: "))
    else:
        print("Selamat anda benar")
        break