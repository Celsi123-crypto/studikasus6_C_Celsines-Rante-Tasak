# studikasus6_C_Celsines-Rante-Tasak

<img width="575" height="500" alt="Screenshot 2026-10-08 204800" src="https://github.com/user-attachments/assets/c8d0143c-5b84-408a-a8a4-4a6e6ca8bc85" />
<img width="452" height="419" alt="Screenshot 2026-10-08 204813" src="https://github.com/user-attachments/assets/cd9180d7-5445-4c91-9bae-3bf658600765" />

Penjelasan Singkat Kode Program

Program diawali dengan import json untuk menggunakan fungsi JSON dalam membaca dan menyimpan data. Variabel path digunakan untuk menentukan lokasi file studikasus6.json, kemudian open() dan json.load() digunakan untuk membaca data yang sudah tersimpan di dalam file tersebut dan memasukkannya ke variabel data. Fungsi tampil_data() digunakan untuk menampilkan seluruh data barang dengan melakukan perulangan for pada setiap data di dalam data, kemudian menampilkan nama, kode, dan stok barang. Selanjutnya, fungsi tambah_data() digunakan untuk menambahkan barang baru ke dalam data menggunakan data.append(). Setelah data ditambahkan, fungsi simpan_file() menggunakan open() dengan mode "w" dan json.dump() untuk menyimpan perubahan tersebut kembali ke file JSON agar data tersimpan secara permanen. Pada bagian utama program, while True digunakan agar menu dapat dijalankan terus-menerus. Pengguna diberikan tiga pilihan, yaitu melihat data barang, menambah barang, atau keluar dari program. Jika memilih menu tambah barang, pengguna diminta memasukkan nama, kode, dan jumlah stok, kemudian data ditambahkan dan disimpan ke file. Jika memilih menu keluar, perulangan dihentikan menggunakan break, sedangkan pilihan yang tidak sesuai akan menampilkan pesan bahwa pilihan tidak tersedia

<img width="610" height="509" alt="Screenshot 2026-10-08 204624" src="https://github.com/user-attachments/assets/23712a98-0c32-47de-ae6e-c8c1e2b66be8" />
<img width="613" height="422" alt="Screenshot 2026-10-08 204642" src="https://github.com/user-attachments/assets/4c8d9628-0058-479f-9a57-0d9310e5fdef" />
