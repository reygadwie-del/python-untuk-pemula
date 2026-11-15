# Class dan Object

class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("Jurusan:", self.jurusan)

mahasiswa1 = Mahasiswa("Ega", "PPLG")

mahasiswa1.tampilkan_data()
