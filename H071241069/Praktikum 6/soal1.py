inventori = {}

while True:
    print("=== Menu Inventori Barang ===")
    print("1. Tambah Barang\n2. Hapus Barang\n3. Tampilkan Barang\n4. Cari Barang\n5. Update Barang\n6. Keluar")
    pilihan = input("Pilih Opsi (1-6): ")

    if pilihan == "1":
        kode = input("Masukkan kode barang: ")
        nama = input("Masukkan nama barang: ")
        jumlah = input("Masukkan jumlah barang: ")
        harga = input("Masukkan harga per unit: ")

        inventori[kode] = {'nama':nama,'jumlah':jumlah,'harga':harga}
        print("Barang berhasil ditambahkan")
    
    elif pilihan == "2":
        kode = input("Masukkan kode barang yang ingin dihapus: ")
        if kode in inventori:
            del inventori[kode]
            print("Barang berhasil dihapus.")
        else:
            print("Kode barang tidak ditemukan di dalam inventori")
    
    elif pilihan == "3":
        if inventori:
            for kode, info_barang in inventori.items():
                print(f"Kode: {kode}, Nama: {info_barang['nama']}, Jumlah: {info_barang['jumlah']}, Harga per unit: {info_barang['harga']}")
        else:
            print("Inventori kosong.")

    elif pilihan == "4":
        pilihan_cari = input("Cari berdasarkan (1) Kode atau (2) Nama: ")
        
        if pilihan_cari == "1":
            kode = input("Masukkan kode barang: ")
            if kode in inventori:
                info_barang = inventori[kode]
                print(f"Kode: {kode}, Nama: {info_barang['nama']}, Jumlah: {info_barang['jumlah']}, Harga per unit: {info_barang['harga']}")
            else:
                print("Barang tidak ditemukan")

        elif pilihan_cari == "2":
            nama = input("Masukkan nama barang: ")
            ditemukan = False

            for kode, info_barang in inventori.items():
                if nama == info_barang["nama"]:
                    print(f"Kode: {kode}, Nama: {info_barang['nama']}, Jumlah: {info_barang['jumlah']}, Harga per unit: {info_barang['harga']}")
                    ditemukan = True
                    break

            if not ditemukan:
                print("Barang tidak ditemukan")

    elif pilihan == "5":
        kode = input("Masukkan kode barang: ")
        if kode in inventori:
            jumlah = input("Masukkan jumlah baru: ")
            harga = input("masukkan harga per unit baru: ")
            
            inventori[kode] = {'nama':nama,'jumlah':jumlah,'harga':harga}
            print("Data barang berhasil diperbarui")
    
    elif pilihan == "6":
        break