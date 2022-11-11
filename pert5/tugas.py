class table:
    
    # class attribute
    nt = "Toko PBO Bahagia"
    
    # instance attribute
    #setter
    def __init__ (self, id_produk, nama_produk, harga, jumlah):
        self.id_produk = id_produk   
        self.nama_produk = nama_produk 
        self.harga = harga
        self.jumlah = jumlah


# instance Mahasiswa class
da = table(2898768, 'NYK Nemesis', 680000, 2)

# access the class attributes
print("Invoice {}".format(da.nt))

# access the instance attributes
print("ID Produk : {}".format(da.id_produk))
print("Nama Produk : {}".format(da.nama_produk))
print("Harga : {}".format(da.harga))
print("Jumlah : {}".format(da.jumlah))