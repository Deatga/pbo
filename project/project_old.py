import tkinter as tk
from tkinter import ttk

class Plant:
    def __init__(self):
        self.statusTumbuh = 0
        self.jumlahAir = 0
        self.jumlahPupuk = 0

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
        tImagePath = "img/seed.webp"
        if self.statusTumbuh == 0:
            tImagePath = "img/seed.webp"
        elif self.statusTumbuh == 1:
            tImagePath = "img/sprout.webp"
        elif self.statusTumbuh == 2:
            tImagePath = "img/small.webp"
        elif self.statusTumbuh == 3:
            tImagePath = "img/big.webp"
        else:
            tImagePath = "img/blossom.webp"
        return tImagePath


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

        # Add text field
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
        self.label.config(image=tk.PhotoImage(file=self.plant.get_image_path()))

if __name__ == "__main__":
        app = PlantMainSwing()
        app.mainloop()



