# PA-DDP-KEL-8

# PROFIL KELOMPOK 8

Muhammad Arzad 2509116014

Kenny Giovanni Gavra 2509116003

Mohammed Rifqy Syahdi 2509116037

# DESKRIPSI SIKNGKAT

Program ini adalah sistem manajemen pertanian sayuran yang memungkinkan dua jenis pengguna (petani dan pelanggan) untuk mengelola dan membeli sayuran secara digital.

# Cara Menjalankan Program

**Install PIP**

- pip install prettytable
<img width="1053" height="158" alt="image" src="https://github.com/user-attachments/assets/43e8eb78-3a10-4764-8971-35602aea5705" />

- pip instal pwinput
<img width="887" height="142" alt="image" src="https://github.com/user-attachments/assets/10d5179c-ee96-4e71-8ed8-076a72b758a3" />

# Fitur Pengguna

**1. Petani**

Fitur yang tersedia:

- Lihat daftar sayuran

- Tambah sayuran baru

- Update informasi sayuran

- Hapus sayuran

**2. Pelanggan**

Fitur yang tersedia:

-  Lihat daftar sayuran

- Cari sayuran berdasarkan nama

- Cek saldo e-money

- Isi saldo e-money

- Beli sayuran

# Struktur Data

**1. data_tanaman.json**

Menyimpan data akun tanaman:

<img width="1412" height="656" alt="image" src="https://github.com/user-attachments/assets/f090d834-d850-467b-ac2d-f0f844ace000" />

**2. data_petani.json**

Menyimpan data akun petani:

<img width="1422" height="163" alt="image" src="https://github.com/user-attachments/assets/827d3cae-987a-4eb6-a803-441137d267ad" />

**3. data_pelanggan.json**

Menyimpan data akun pelanggan:

<img width="1420" height="177" alt="image" src="https://github.com/user-attachments/assets/1d7732c1-8428-4c3a-b09b-e9f257e227dd" />

# Panduan Penggunaan

**Registrasi Akun Baru**

**1. Buat Akun Petani**

<img width="493" height="250" alt="image" src="https://github.com/user-attachments/assets/7e3b7cab-761b-4d79-9d01-8e83a7096e42" />

- Pilih opsi "2" di menu utama

- Masukkan username dan password

- Akun akan tersimpan di data_petani.json

**2. Buat Akun Pelanggan**

<img width="502" height="250" alt="image" src="https://github.com/user-attachments/assets/1eb4f738-948c-4e11-9993-de8fdb84f1d4" />


- Pilih opsi "3" di menu utama

- Masukkan username dan password

- Akun akan tersimpan di data_pelanggan.json dengan saldo awal 0

**Login**

<img width="493" height="271" alt="image" src="https://github.com/user-attachments/assets/8618ed97-6ae2-487a-904e-e4b5fc316c58" />

- Pilih opsi "1" di menu utama

- Masukkan username dan password

- Sistem akan mengarahkan ke menu sesuai role (petani/pelanggan)

**Menu Petani**

**1. Lihat Sayuran**

<img width="297" height="342" alt="image" src="https://github.com/user-attachments/assets/43640f22-1c88-49a3-8f56-35b9e7c95c0f" />


- Menampilkan tabel semua sayuran yang tersedia

- Menampilkan ID, nama, harga, dan stok

**2. Tambah Sayuran**

<img width="241" height="235" alt="image" src="https://github.com/user-attachments/assets/dbbba915-968d-4d22-949b-f2e884b26b3b" />

- Input nama sayuran

- Input harga (harus angka)

- Input stok (harus angka)

- ID akan otomatis ter-generate

**3. Update Sayuran**

<img width="358" height="323" alt="image" src="https://github.com/user-attachments/assets/27a846e5-da60-4854-9609-15a1bce4f061" />

- Pilih ID sayuran yang akan diupdate

- Bisa update nama, harga, atau stok

- Kosongkan field jika tidak ingin mengubah

**4. Hapus Sayuran**

<img width="285" height="286" alt="image" src="https://github.com/user-attachments/assets/9d20299a-fd40-4d52-b657-c730d0a68c69" />

**Menu Pelanggan**

**1. Lihat Sayuran**
- Menampilkan semua sayuran yang tersedia

**2. Cari Tanaman**
Cari sayuran berdasarkan nama

Menampilkan hasil pencarian dalam tabel

**3. Cek Saldo**
- Menampilkan saldo e-money saat ini

**4. Isi Saldo**
- Input jumlah saldo yang akan diisi

Saldo akan bertambah sesuai input

**5. Beli Tanaman**
- Pilih ID sayuran yang ingin dibeli

- Input jumlah (kg) yang ingin dibeli

- Sistem akan menghitung total harga

- Konfirmasi pembelian

- Jika saldo cukup, transaksi akan diproses

- Stok sayuran dan saldo akan otomatis terupdate

- Pilih ID sayuran yang akan dihapus

- Konfirmasi penghapusan






