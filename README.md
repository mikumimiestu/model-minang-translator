<!-- Logo Python dan SQLite -->
<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" width="180"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/SQLite370.svg" alt="SQLite Logo" width="100"/>
</p>

# Minang Translator Model

Minang Translator Model adalah aplikasi berbasis terminal untuk menerjemahkan kata atau kalimat dari Bahasa Indonesia/Inggris ke Bahasa Minang. Model ini juga mendukung penambahan data baru ke dalam database SQLite lokal.

---

# Bahsa Pemrograman

Bahasa pemrograman yang digunakan dalam aplikasi ini adalah Python.

---

# Database

Database yang digunakan dalam aplikasi ini adalah SQLite.

---

## 📦 Setup Virtual Environment

### Buat environment baru

```bash
python -m venv myenv

# atau

python3 -m venv myenv
```

### Aktifkan environment

```bash
# di Linux/Mac
source myenv/bin/activate

# di Windows

myenv\Scripts\activate
```

### ▶️ Jalankan Program

```bash
python main.py
```

# ✍️ Fitur

1. Translate kata atau kalimat dari Indonesia/Inggris ke Minang
2. Tambah data baru ke database
3. Validasi input dan penanda jika kata belum tersedia

# 📂 Struktur Folder

```bash
minang-translator/
│
├── main.py
├── kamus.db
├── model/
│   └── MinangBrain.py
└── myenv/ (virtual environment)
```

# 📝 Dokumentasi

- [ ] Dokumentasi kode
- [ ] Dokumentasi database
- [ ] Dokumentasi API (jika ada)
- [ ] Dokumentasi penggunaan aplikasi
- [ ] Dokumentasi pengembangan aplikasi
- [ ] Dokumentasi pengujian aplikasi
- [ ] Dokumentasi pengembangan aplikasi

# Copyright

Mikumiestu (2025) - [mikumiestu@technovagroupinc.com](mailto:mikumiestu@technovagroupinc.com)

Distribusi bebas dengan lisensi MIT. Lihat `LICENSE` untuk informasi lebih lanjut.
