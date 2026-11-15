# Lists dan Dictionaries

buah = ["Apel", "Jeruk", "Mangga"]

print("Daftar Buah:")
for item in buah:
    print(item)

buah.append("Pisang")
print("Setelah ditambahkan:", buah)

mahasiswa = {
    "nama": "Ega",
    "kelas": "XI",
    "jurusan": "PPLG"
}

print("\nData Mahasiswa:")
print("Nama:", mahasiswa["nama"])
print("Kelas:", mahasiswa["kelas"])
print("Jurusan:", mahasiswa["jurusan"])
