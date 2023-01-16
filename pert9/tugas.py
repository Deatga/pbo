class plant:
    def __init__(self,name,jenis_tumbuhan,nama_ilmiah,kelas):
        self.name = name
        self.jenis_tumbuhan = jenis_tumbuhan
        self.nama_ilmiah = nama_ilmiah
        self.kelas = kelas

    def show (self):
        print("{}\n\t jenis Tumbuhan : {}\n\t nama ilmiah    : {}\n\t kelas bunga    : {} \n\t ". format(self.name,self.jenis_tumbuhan,self.nama_ilmiah,self.kelas))
    
    def perkembangan (self):
        print("Pertumbuhan tumbuhan ini dalam kondisi baik")

    def perkembanan_buruk (self):
        print("Pertumbuhan tumbuhan ini dalam kondisi buruk")

class plant_anggrek(plant):
      def __init__(self,name,jenis_tumbuhan,nama_ilmiah,kelas):
        super().__init__(name,jenis_tumbuhan,nama_ilmiah,kelas)
        super().show()
        super().perkembanan_buruk

class plant_mawar(plant):
    def __init__(self,name,jenis_tumbuhan,nama_ilmiah,kelas):
        super().__init__(name,jenis_tumbuhan,nama_ilmiah,kelas)
        super().show()
        super().perkembangan

class plant_melati(plant):
    def __init__(self,name,jenis_tumbuhan,nama_ilmiah,kelas):
        super().__init__(name,jenis_tumbuhan,nama_ilmiah,kelas)
        super().show()
        super().perkembanan_buruk

 
anggrek = plant_anggrek('anggrek','tumbuhan hias','Orchidaceae','Liliopsida')
mawar = plant_mawar('Mawar','Tumbuhan Hias','Rosa','Dicotyledona')
melati = plant_melati('Melati','Tumbuhan Hias','Jasminum','Magnoliopsida')








        

        