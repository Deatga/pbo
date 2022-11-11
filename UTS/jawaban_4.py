def jual():
    a = "Capcin"
    b = "Matcha"
    print ("Menu")
    print ("1.", a)
    print ("2.", b)
    print ("3. Exit")

def capcin():
    cap = "Memilih capucino"
    print(cap)
    capucino = int(input("masukkan harga : "))
    ppn = capucino*10/100
    total = capucino+ppn
    print(total)

def teh():
    te = "memilih TEH"
    print(te)
    teh = int(input("masukkan harga : "))
    ppn = teh*10/100
    total = teh+ppn
    print(total)

def nama_nim():
    nim = 1234567
    nama = "QWERTY"
    print ("NIM : ", nim)
    print ("NAMA : ", nama)

while True:
    nama_nim()
    jual()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capcin()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print ("pilihan salah")