from model.MinangBrain import MinangBrain

def menu():
    print("\n=== MINANG TRANSLATOR ===")
    print("1. Tranlate ke Minang")
    print("2. Tambah data baru")
    print("0. Keluar")

def main():
    brain = MinangBrain()
    while True:
        menu()
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            asal = input("Masukkan bahasa asal (Indonesia / Inggris): ").strip().lower()
            kata = input(f"Teks {asal.title()}: ")
            hasil = brain.cari_terjemahan(kata, asal)
            if hasil:
                print(f"Terjemahan Minang: {hasil}")
            else:
                print("Data tidak ditemukan")
        
        elif pilihan == "2":
            