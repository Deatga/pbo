class table:
    
    # class attribute
    nt = "Toko PBO Bahagia"
    
    # instance attribute
    #setter
    def _init_ (self, id_produk, nama_produk, harga, jumlah):
        self.id_produk = id_produk   
        self.nama_produk = nama_produk 
        self.harga = harga
        self.jumlah = jumlah

    @property
    
