import sqlite3

class MinangBrain:
    def __init__(self, db_path="kamus.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS kamus (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                minang TEXT,
                                indonesia TEXT,
                                inggris TEXT)''')
        self.conn.commit()

    def tambah_data(self, minang, indonesia, inggris):
        self.cursor.execute("INSERT INTO kamus (minang, indonesia, inggris) VALUES (?, ?, ?)",
                            (minang.lower(), indonesia.lower(), inggris.lower()))
        self.conn.commit()

    def cari_terjemahan(self, teks, asal):
        # kalau input hanya satu kata
        teks = teks.strip().lower()
        self.cursor.execute(f"SELECT minang FROM kamus WHERE {asal} = ?", (teks,))
        hasil = self.cursor.fetchone()
        return hasil[0] if hasil else None

    def translate_kalimat(self, kalimat, asal):
        kata_list = kalimat.lower().split()
        hasil_terjemah = []

        for kata in kata_list:
            self.cursor.execute(f"SELECT minang FROM kamus WHERE {asal} = ?", (kata,))
            hasil = self.cursor.fetchone()
            if hasil:
                hasil_terjemah.append(hasil[0])
            else:
                hasil_terjemah.append(f"[{kata}]")  # penanda kata yang belum ada
        return " ".join(hasil_terjemah)

    def tutup(self):
        self.conn.close()
