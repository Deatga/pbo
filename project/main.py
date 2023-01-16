import tkinter as tk
from tkinter import ttk
import mysql.connector

class Plant:
    def __init__(self):
        self.statusTumbuh = 0
        self.jumlahAir = 0
        self.jumlahPupuk = 0
        
    def get_jumlah_air(self):
        return self.jumlah_air
    
    def set_jumlah_air(self, jumlah_air):
        self.jumlah_air = jumlah_air
    
    def get_jumlah_pupuk(self):
        return self.jumlah_pupuk
    
    def set_jumlah_pupuk(self, jumlah_pupuk):
        self.jumlah_pupuk = jumlah_pupuk
    
    def set_status_tumbuh(self, status_tumbuh):
        self.status_tumbuh = status_tumbuh

    def beri_air(self):
        self.jumlahAir += 1
        self.cek_kondisi_tumbuh()

    def beri_pupuk(self):
        self.jumlahPupuk += 1
        self.cek_kondisi_tumbuh()

    def cek_kondisi_tumbuh(self):
        if self.jumlahAir >= 3 and self.jumlahPupuk >= 1:
            self.tumbuh()

    def tumbuh(self):
        if self.statusTumbuh < 4:
            self.jumlahAir -= 3
            self.jumlahPupuk -= 1
            self.statusTumbuh += 1

    def display_plant(self):
        print(self.get_status_tumbuh_text())
        print("Jumlah Air:" + str(self.jumlahAir))
        print("Jumlah Pupuk:" + str(self.jumlahPupuk))

    def get_status_tumbuh_text(self):
        if self.statusTumbuh == 0:
            return "Benih"
        elif self.statusTumbuh == 1:
            return "Tunas"
        elif self.statusTumbuh == 2:
            return "Tanaman Kecil"
        elif self.statusTumbuh == 3:
            return "Tanaman Dewasa"
        else:
            return "Berbunga"

    def get_status_tumbuh(self):
        return self.statusTumbuh

    def get_image_path(self):
        tImagePath = "project/gambar/seed.png"
        if self.statusTumbuh == 0:
            tImagePath = "project/gambar/seed.png"
        elif self.statusTumbuh == 1:
            tImagePath = "project/gambar/sprout.png"
        elif self.statusTumbuh == 2:
            tImagePath = "project/gambar/small.png"
        elif self.statusTumbuh == 3:
            tImagePath = "project/gambar/big.png"
        else:
            tImagePath = "project/gambar/blossom.png"
        return tImagePath

class UgardenMain(tk.Tk):
    def __init__(self):
        super().__init__()

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plant"
        )

        self.title("WELCOME TO UGARDEN")
        self.geometry("500x300")
        self.resizable(False, False)

        # Add label
        self.label = tk.Label(self, text="Welcome To Ugarden")
        self.label = tk.Label(self, text="Silakan masukan nama anda untuk memilih tanaman anda :")
        self.label.pack()

        # Add buttons
        self.nama_textfield = tk.Entry(self)
        self.nama_textfield.insert(0, 'Masukan nama')
        self.nama_textfield.bind("<FocusIn>", lambda args: self.nama_textfield.delete(0,'end'))
        self.nama_textfield.pack()

        ttk.Button(self, text="Anggrek", command=self.openAnggrekWindows).pack()
        ttk.Button(self, text="Mawar", command=self.openMawarWindows).pack()
        ttk.Button(self, text="Melati", command=self.openMelatiWindows).pack()        

    def tambah(self):
        # Membuat cursor
        cursor = self.db.cursor()

        # Memasukkan data ke tabel "tanaman"
        nama = self.nama_textfield.get()
        sql = "INSERT INTO name (name) VALUES (%s)"
        val = (nama,)
        cursor.execute(sql, val)

        # Menyimpan perubahan ke database
        self.db.commit()

    def openAnggrekWindows(self):
        if __name__ == "__main__":
            self.tambah()
            self.anggrek = PlantMainSwing()
            self.anggrek.mainloop()

    def openMawarWindows(self):
        if __name__ == "__main__":
            self.tambah()
            self.melati = PlantMainSwing()
            self.melati.mainloop()

    def openMelatiWindows(self):
        if __name__ == "__main__":
            self.tambah()
            self.mawar = PlantMainSwing()
            self.mawar.mainloop()

class PlantMainSwing(tk.Tk):
    def __init__(self):
        super().__init__()

        self.plant = Plant()

        self.title("WELCOME TO UGARDEN")
        self.geometry("500x300")
        self.resizable(False, False)

        # Add label
        self.label = tk.Label(self, text="")
        self.label.pack()

        # Add buttons
        ttk.Button(self, text="Beri Air", command=self.give_water).pack()
        ttk.Button(self, text="Beri Pupuk", command=self.give_fertilizer).pack()

        # Add widget
        self.text_field = tk.Text(self, width=20, height=1)
        self.text_field.pack()
        self.set_plant_image()

    def give_water(self):
        self.plant.beri_air()
        self.text_field.delete("1.0", tk.END)
        self.text_field.insert("1.0", self.plant.get_status_tumbuh_text())
        self.set_plant_image()

    def give_fertilizer(self):
        self.plant.beri_pupuk()
        self.text_field.delete("1.0", tk.END)
        self.text_field.insert("1.0", self.plant.get_status_tumbuh_text())
        self.set_plant_image()

    def set_plant_image(self):
        self.photo = tk.PhotoImage(file = self.plant.get_image_path()) 
        self.label.config(image=self.photo)

if __name__ == "__main__":
    app = UgardenMain()
    app.mainloop()



