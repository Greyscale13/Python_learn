import random
while True:
    a = random.randrange(1,4)
    if a == 1:
        com = "gunting"
    elif a == 2:
        com = "batu"
    else:
        com = "kertas"
    ym = input("Your Move (gunting, batu, kertas) : ")
    if ym == "gunting" and com == "batu":
        print("Kalah :p")
        njut = input("Mau main lagi? (yes or no)")
        if njut == "yes":
            continue
        else:
            break
    elif ym == "gunting" and com == "kertas":
        print("Menang woohoo")
        njut = input("Mau main lagi? (yes or no)")
        if njut == "yes":
            continue
        else:
            break
    elif ym == "gunting" and com == "gunting":
        print("Seri, coba lagi")
    elif ym == "kertas" and com == "batu":
        print("Menang woohoo")
        njut = input("Mau main lagi? (yes or no) : ")
        if njut == "yes":
            continue
        else:
            break
    elif ym == "kertas" and com == "kertas":
        print("Seri, coba lagi")
    elif ym == "kertas" and com == "gunting":
        print("Kalah :p")
        njut = input("Mau main lagi? (yes or no) : ")
        if njut == "yes":
            continue
        else:
            break
    elif ym == "batu" and com == "batu":
        print("Seri, coba lagi")
    elif ym == "batu" and com == "kertas":
        print("Kalah :p")
        njut = input("Mau main lagi? (yes or no) : ")
        if njut == "yes":
            continue
        else:
            break
    elif ym == "batu" and com == "gunting":
        print("Menang woohoo")
        njut = input("Mau main lagi? (yes or no) : ")
        if njut == "yes":
            continue
        else:
            break
    else:
        break