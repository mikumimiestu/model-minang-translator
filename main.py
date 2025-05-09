from model.MinangBrain import MinangBrain

def menu():
    print("\n=== MINANG TRANSLATOR ===")
    print("1. Translate ke Minang")
    print("2. Tambah data baru")
    print("0. Keluar")

def main():
    brain = MinangBrain()
    while True:
        menu()
        pilihan = input("Pilih opsi: ").strip()
        
        if pilihan == "1":
            asal = input("Masukkan bahasa asal (indonesia / inggris): ").strip().lower()
            if asal not in ["indonesia", "inggris"]:
                print("Bahasa tidak valid. Hanya bisa 'indonesia' atau 'inggris'.")
                continue

            teks = input(f"Teks {asal.title()}: ").strip()

            if " " in teks:  # jika input adalah kalimat
                hasil = brain.translate_kalimat(teks, asal)
                print(f"Terjemahan Kalimat Minang:\n→ {hasil}")
            else:
                hasil = brain.cari_terjemahan(teks, asal)
                if hasil:
                    print(f"Terjemahan Minang: {hasil}")
                else:
                    print("Kata tidak ditemukan.")
        
        elif pilihan == "2":
            minang = input("Minang: ")
            indo = input("Indonesia: ")
            inggris = input("Inggris: ")
            brain.tambah_data(minang, indo, inggris)
            print("Data berhasil ditambahkan.")
        
        elif pilihan == "0":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid.")

    brain.tutup()

if __name__ == "__main__":
    main()
