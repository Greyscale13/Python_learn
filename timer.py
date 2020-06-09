import time
menit = int(input("Masukkan menit yang anda mau : "))
detik = int(input("Masukkan detik yang anda mau : "))

totmin = menit*60
totdet = totmin + detik

for x in reversed (range (totdet+1)):
    print(str(x) + " detik sisa waktu anda")
    totdet -= 1
    time.sleep(1)
print("Waktu sudah habis")