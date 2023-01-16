import tkinter as tk
import mysql.connector

class AplikasiGUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Koneksi ke database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plant"
        )

         # Membuat textfield
        self.nama_textfield = tk.Entry(self)
        self.nama_textfield.pack()

        # Membuat tombol Tambah
        self.tambah_button = tk.Button(self, text="Tambah", command=self.tambah)
        self.tambah_button.pack()

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

        # Menampilkan pesan
        tk.messagebox.showinfo("Pesan", "Data berhasil ditambahkan ke database.")

if __name__ == "__main__":
    root = tk.Tk()
    AplikasiGUI(root).pack()
    root.mainloop()