# LockMail

LockMail adalah aplikasi GUI berbasis Python dan Tkinter (menggunakan `ttkbootstrap`) yang digunakan untuk mengenkripsi dan mendekripsi isi email menggunakan algoritma sandi Vigenère. Aplikasi ini dirancang agar sederhana dan mudah digunakan untuk menjaga keamanan pesan teks.

## Fitur

- 🔐 Enkripsi teks dengan kunci rahasia menggunakan algoritma Vigenère.
- 🔓 Dekripsi teks yang telah dienkripsi.
- 📋 Salin hasil enkripsi/dekripsi langsung ke clipboard.
- 💻 Antarmuka grafis modern dengan `ttkbootstrap`.

## Instalasi

1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/lockmail.git
   cd lockmail
   ```

2. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan aplikasi:
   ```bash
   python main.py
   ```

## Struktur Folder

```
LockMail/
│
├── vigenere.py               # Algoritma enkripsi dan dekripsi Vigenère
├── clipboard_utils.py        # Utilitas untuk menyalin teks ke clipboard
├── main.py                   # Antarmuka utama GUI aplikasi
├── tests/
│   └── test_vigenere.py      # Unit test untuk modul Vigenère
├── LockMail_Documentation.md # Dokumentasi utama aplikasi
└── README.md                 # Dokumentasi singkat proyek ini
```

## Pengujian

Untuk menjalankan pengujian:
```bash
python -m unittest discover tests
```

## Lisensi

Aplikasi ini dikembangkan untuk kebutuhan pembelajaran dan distribusi internal. Gunakan dengan bijak.