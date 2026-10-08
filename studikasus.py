import json

path = r"C:\Users\ACER\OneDrive\praktikum vscode\Json\studikasus6.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)


def tampil_data():
    print("\n=== DATA INVENTARIS BARANG ===")

    for barang in data:
        print("Nama  :", barang["nama"])
        print("Kode  :", barang["kode"])
        print("Stok  :", barang["stok"])
        print("------------------------")


def tambah_data(nama, kode, stok):
    data.append({
        "nama": nama,
        "kode": kode,
        "stok": stok
    })

    return "Data berhasil ditambahkan!"


def simpan_file():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return "Data berhasil disimpan!"


while True:
    print("\n===== SISTEM INVENTARIS BARANG =====")
    print("1. Lihat Data Barang")
    print("2. Tambah Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampil_data()

    elif pilihan == "2":
        nama = input("Masukkan nama barang: ")
        kode = input("Masukkan kode barang: ")
        stok = int(input("Masukkan jumlah stok: "))

        print(tambah_data(nama, kode, stok))
        print(simpan_file())

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")