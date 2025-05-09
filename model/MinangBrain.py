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

    def tambah_date(self, minang, indonesia, inggris):
        self.cursor.execute("INSERT INTO kamus (minang, indonesia, inggris) VALUES (?, ?, ?)",
                            (minang.lower(), indonesia.lower(), inggris.lower()))
        
        self.conn.commit()

    def cari_terjemahan(self, teks, asal):
        self.cursor.execute(f"SELECT minang FROM kamus WHERE {asal} = ?", (teks.lower(),))
        hasil = self.cursor.fetchone()
        return hasil [0] if hasil else None
    
    def tutup(self):
        self.conn.close()