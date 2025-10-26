import json
from prettytable import PrettyTable
import pwinput

'''=================================================================================================================================='''
'''                                                         JSON                                                                     '''
'''=================================================================================================================================='''

def BacaData(namafile):
    try:
        with open(namafile, 'r') as f:
            return json.load(f)
    except:
        return []

def SimpanData(data, namafile):
    with open(namafile, 'w') as f:
        json.dump(data, f, indent=2)
    return True

'''=================================================================================================================================='''
'''                                                   BUAT AKUN PETANI                                                               '''         
'''=================================================================================================================================='''

def buat_akun_petani():
    print("===== BUAT AKUN PETANI =====")
    
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")
    
    petani = BacaData("Penugasan Akhir Kelompok 8.py\data_petani.json")

    petani_baru = {
        "username": username, 
        "password": password,
        "role": "petani"
    }
    
    petani.append(petani_baru)
    SimpanData(petani, "Penugasan Akhir Kelompok 8.py\data_petani.json")
    
    return petani_baru

'''=================================================================================================================================='''
'''                                                   BUAT AKUN PELANGGAN                                                            '''         
'''=================================================================================================================================='''

def buat_akun_pelanggan():
    print("===== BUAT AKUN PELANGGAN =====")
    
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")
    
    pelanggan = BacaData("Penugasan Akhir Kelompok 8.py\data_pelanggan.json")

    pelanggan_baru = {
        "username": username, 
        "password": password,
        "saldo": 0,
        "role": "pelanggan"
    }
    
    pelanggan.append(pelanggan_baru)
    SimpanData(pelanggan, "Penugasan Akhir Kelompok 8.py\data_pelanggan.json")
    
    return pelanggan_baru

'''=================================================================================================================================='''
'''                                                        LOGIN                                                                     '''         
'''=================================================================================================================================='''

def login():
    print(f"\n ===== LOGIN =====")
    
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")
    
    petani = BacaData("Penugasan Akhir Kelompok 8.py\data_petani.json")
    for p in petani:
        if p["username"] == username and p["password"] == password:
            print(f"Login berhasil Selamat datang {username}")
            return {"username": username, "role": "petani"}
    
    pelanggan = BacaData("Penugasan Akhir Kelompok 8.py\data_pelanggan.json")
    for p in pelanggan:
        if p["username"] == username and p["password"] == password:
            print(f"Login berhasil Selamat datang {username}")
            return {"username": username, "role": "pelanggan", "saldo": p["saldo"]}
    
    print("Login gagal Username atau password salah")
    return None

'''=================================================================================================================================='''
'''                                                     MENU PETANI                                                                  '''         
'''=================================================================================================================================='''

def petani_menu(user):
    while True:
        print(f"\n ===== MENU PETANI =====")
        print("1. Lihat Sayuran")
        print("2. Tambah Sayuran") 
        print("3. Update Sayuran")
        print("4. Hapus Sayuran")
        print("5. Keluar")
        print("===========================")
        
        pilih = input("Pilih menu: ")

        if pilih == "1":
            lihat_tanaman()
        elif pilih == "2":
            tambah_tanaman()
        elif pilih == "3":
            update_tanaman()
        elif pilih == "4":
            hapus_tanaman()
        elif pilih == "5":
            break
        else:
            print("Pilihan salah")

'''=================================================================================================================================='''
'''                                                      MENU PELANGGAN                                                              '''         
'''=================================================================================================================================='''

def menu_pelanggan(user):
    while True:
        print(f"\n ===== MENU PELANGGAN =====")
        print("1. Lihat ")
        print("2. Cari Tanaman")
        print("3. Cek Saldo")
        print("4. Isi Saldo")
        print("5. Beli Tanaman")
        print("6. Keluar")
        print("==============================")
        
        pilih = input("Pilih menu: ")
        
        if pilih == "1":
            lihat_tanaman()
        elif pilih == "2":
            cari_tanaman()
        elif pilih == "3":
            cek_saldo(user)
        elif pilih == "4":
            isi_saldo(user)
        elif pilih == "5":
            beli_tanaman(user)
        elif pilih == "6":
            break
        else:
            print("Pilihan salah")

'''=================================================================================================================================='''
'''                                                   LIHAT TANAMAN                                                                  '''         
'''=================================================================================================================================='''

def lihat_tanaman():
    tanaman = BacaData("Penugasan Akhir Kelompok 8.py\data_tanaman.json")
    
    if not tanaman:
        print("Tidak ada data tanaman!")
        return
    
    table = PrettyTable()
    table.title = "Data Sayuran"
    table.field_names = ["ID", "Nama", "Harga", "Stok"]

    for t in tanaman:
        table.add_row([t["id"], t["nama"], f"Rp{t['harga']:,}", t["stok"]])

    print(table)

'''=================================================================================================================================='''
'''                                                  TAMBAH TANAMAN                                                                  '''         
'''=================================================================================================================================='''

def tambah_tanaman():
    print(" ===== TAMBAH TANAMAN ===== ")
    tanaman = BacaData("Penugasan Akhir Kelompok 8.py\data_tanaman.json")

    if tanaman:
        id_baru = max(t["id"] for t in tanaman) + 1
    else:
        id_baru = 1
        
    nama = input("Nama tanaman: ")
    
    try:
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
    
    except ValueError:
        print("Harga dan stok harus angka")
        return
            
    tanaman_baru = {
        "id": id_baru,
        "nama": nama, 
        "harga": harga, 
        "stok": stok
    }
    
    tanaman.append(tanaman_baru)
    SimpanData(tanaman, "Penugasan Akhir Kelompok 8.py\data_tanaman.json")
    print("Tanaman berhasil ditambahkan") 

'''=================================================================================================================================='''
'''                                                  UPDATE TANAMAN                                                                  '''         
'''=================================================================================================================================='''

def update_tanaman():
    print(f"\n ===== UPDATE TANAMAN =====")
    
    tanaman = BacaData("Penugasan Akhir Kelompok 8.py\data_tanaman.json")
    
    if not tanaman:
        print("Tidak ada data tanaman")
        return
    
    lihat_tanaman()
    
    try:
        id_update = int(input("ID tanaman yang diupdate: "))
        
        for t in tanaman:
            if t["id"] == id_update:
                print(f"Data saat ini: {t['nama']} - Rp{t['harga']:,} - Stok: {t['stok']}")
                
                nama_baru = input("Nama baru: ")
                harga_baru = input("Harga baru: ")
                stok_baru = input("Stok baru: ")
                
                if nama_baru:
                    t["nama"] = nama_baru
                if harga_baru:
                    t["harga"] = int(harga_baru)
                if stok_baru:
                    t["stok"] = int(stok_baru)
                
                SimpanData(tanaman, "Penugasan Akhir Kelompok 8.py\data_tanaman.json")
                print("Tanaman berhasil diupdate!")
                return
        
        print("ID tidak ditemukan")
        
    except ValueError:
        print("Input harus angka")

'''=================================================================================================================================='''
'''                                                  HAPUS TANAMAN                                                                   '''         
'''=================================================================================================================================='''

def hapus_tanaman():
    print(f"\n ===== HAPUS TANAMAN =====")
    tanaman = BacaData("Penugasan Akhir Kelompok 8.py\data_tanaman.json")
    
    if not tanaman:
        print("Tidak ada tanaman")
        return
    
    lihat_tanaman()
    
    try:
        hapus_id = int(input("ID tanaman yang dihapus: "))
        
        for h, t in enumerate(tanaman):
            if t["id"] == hapus_id:
                konfirmasi = input(f"Yakin hapus {t['nama']}? (y/n): ").lower()
                if konfirmasi == 'y':
                    tanaman.pop(h)
                    SimpanData(tanaman, "Penugasan Akhir Kelompok 8.py\data_tanaman.json")
                    print("Tanaman berhasil dihapus")
                else:
                    print("Penghapusan dibatalkan")
                return
        
        print("ID tidak ditemukan")
        
    except ValueError:
        print("ID harus angka")

'''=================================================================================================================================='''
'''                                                  CARI TANAMAN                                                                    '''         
'''=================================================================================================================================='''

def cari_tanaman():
    print(f"\n ===== CARI TANAMAN =====")
    tanaman = BacaData("Penugasan Akhir Kelompok 8.py\data_tanaman.json")
    
    if not tanaman:
        print("Tidak ada data tanaman!")
        return
    
    nama_tanaman = input("Cari tanaman (Masukkan nama tanaman yang di cari): ")
    hasil = [t for t in tanaman if nama_tanaman in t["nama"]]
    
    if not hasil:
        print("Tanaman tidak ditemukan")
        return
    
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Harga", "Stok"]
    
    for t in hasil:
        table.add_row([t["id"], t["nama"], f"Rp{t['harga']:,}", t["stok"]])
    
    print(table)

'''=================================================================================================================================='''
'''                                                  CEK SALDO                                                                       '''         
'''=================================================================================================================================='''

def cek_saldo(user):
    print(f"\n ===== CEK SALDO =====")
    print(f"Username: {user['username']}")
    
    # Cek apakah user punya saldo
    if 'saldo' in user:
        print(f"Saldo E-Money: Rp{user['saldo']:,}")
    else:
        print("Saldo E-Money: Rp0")

'''=================================================================================================================================='''
'''                                                  ISI SALDO                                                                       '''         
'''=================================================================================================================================='''

def isi_saldo(user):
    print(f"\n ===== ISI SALDO =====")
    
    # Cek saldo saat ini
    if 'saldo' in user:
        print(f"Saldo E-Money: Rp{user['saldo']:,}")
    else:
        print("Saldo E-Money: Rp0")
    
    try:
        jumlah = int(input("Jumlah isi: "))
        
        if jumlah <= 0:
            print("Jumlah harus > 0!")
            return

        pelanggan = BacaData("Penugasan Akhir Kelompok 8.py\data_pelanggan.json")
        
        for p in pelanggan:
            if p["username"] == user["username"]:
                # Cek apakah pelanggan punya saldo
                if 'saldo' in p:
                    p["saldo"] = p["saldo"] + jumlah
                else:
                    p["saldo"] = jumlah
                break
        
        SimpanData(pelanggan, "Penugasan Akhir Kelompok 8.py\data_pelanggan.json")
        
        # Update saldo di pelanggan
        if 'saldo' in user:
            user["saldo"] = user["saldo"] + jumlah
        else:
            user["saldo"] = jumlah
        
        print(f"Saldo berhasil diisi! Saldo sekarang: Rp{user['saldo']:,}")
        
    except ValueError:
        print("Error: Jumlah harus angka")

'''=================================================================================================================================='''
'''                                                  BELI TANAMAN                                                                    '''         
'''=================================================================================================================================='''

def beli_tanaman(user):
    print(f"\n ===== BELI TANAMAN =====")
    tanaman_list = BacaData("Penugasan Akhir Kelompok 8.py\data_tanaman.json")
    
    if not tanaman_list:
        print("Tidak ada tanaman tersedia!")
        return
    
    lihat_tanaman()
    
    try:
        id_tanaman = int(input("ID tanaman: "))
        jumlah = int(input("Jumlah (kg): "))
        
        if jumlah <= 0:
            print("Jumlah harus > 0!")
            return
        
        # Cari tanaman berdasarkan ID
        tanaman_dipilih = None
        for t in tanaman_list:
            if t["id"] == id_tanaman:
                tanaman_dipilih = t
                break
        
        if not tanaman_dipilih:
            print("Tanaman tidak ditemukan")
            return
        
        if jumlah > tanaman_dipilih["stok"]:
            print(f"Stok tidak cukup! Stok tersedia: {tanaman_dipilih['stok']} kg")
            return
        
        total = jumlah * tanaman_dipilih["harga"]
        
        # Cek saldo user
        saldo_sekarang = 0
        if 'saldo' in user:
            saldo_sekarang = user['saldo']
        
        if total > saldo_sekarang:
            print(f"Saldo tidak cukup Butuh: Rp{total:,}, Saldo: Rp{saldo_sekarang:,}")
            return
        
        print(f"\n RINCIAN PEMBELIAN:")
        print(f"Tanaman   : {tanaman_dipilih['nama']}")
        print(f"Jumlah    : {jumlah} kg")
        print(f"Harga/kg  : Rp{tanaman_dipilih['harga']:,}")
        print(f"Total     : Rp{total:,}")
        print(f"Saldo     : Rp{saldo_sekarang:,}")
        
        konfirmasi = input("Lanjutkan pembelian? (y/n): ")
        
        if konfirmasi.lower() == "y":
            # Update stok tanaman
            for t in tanaman_list:
                if t["id"] == id_tanaman:
                    t["stok"] -= jumlah
                    break
            
            # Update saldo pelanggan
            pelanggan_list = BacaData("Penugasan Akhir Kelompok 8.py\data_pelanggan.json")
            for p in pelanggan_list:
                if p["username"] == user["username"]:
                    if 'saldo' in p:
                        p["saldo"] = p["saldo"] - total
                    else:
                        p["saldo"] = -total
                    break
            
            SimpanData(tanaman_list, "Penugasan Akhir Kelompok 8.py\data_tanaman.json")
            SimpanData(pelanggan_list, "Penugasan Akhir Kelompok 8.py\data_pelanggan.json")
            
            if 'saldo' in user:
                user["saldo"] = user["saldo"] - total
            else:
                user["saldo"] = -total
            
            print("="*50)
            print("           INVOICE PEMBELIAN")
            print("="*50)
            print(f"Produk      : {tanaman_dipilih['nama']}")
            print(f"Jumlah      : {jumlah} kg")
            print(f"Harga/kg    : Rp{tanaman_dipilih['harga']:,}")
            print(f"Total       : Rp{total:,}")
            print(f"Metode      : E-Money")
            print(f"Saldo Awal  : Rp{saldo_sekarang:,}")
            print(f"Saldo Akhir : Rp{user['saldo']:,}")
            print("="*50)
            print("Terima kasih atas pembelian Anda, Silahkan datang kembali")
        else:
            print("Pembelian dibatalkan.")
            
    except ValueError:
        print("Error: Input harus angka")


'''=================================================================================================================================='''
'''                                                  MENU UTAMA                                                                      '''         
'''=================================================================================================================================='''

def main():
    while True:
        print("="*60)
        print(f"\n SELAMAT DATANG DI SISTEM MANAJEMEN PERTANIAN SAYURAN")
        print("="*60)
        print("1. Login")
        print("2. Buat Akun Petani")
        print("3. Buat Akun Pelanggan")
        print("4. Keluar")
        print("="*60)
        
        pilihan = input("Pilih opsi (1-4): ")
        
        if pilihan == "1":
            user = login()
            if user:
                if user["role"] == "petani":
                    petani_menu(user)
                else:
                    menu_pelanggan(user)
                    
        elif pilihan == "2":
            user = buat_akun_petani()
            print("Akun petani berhasil dibuat Silakan login untuk melanjutkan.")
                
        elif pilihan == "3":
            user = buat_akun_pelanggan()
            print("Akun pelanggan berhasil dibuat Silakan login untuk melanjutkan.")
                
        elif pilihan == "4":
            print("Terima kasih")
            break
            
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()