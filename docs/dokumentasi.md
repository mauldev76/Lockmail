
# 📧 LockMail - Aplikasi Enkripsi & Dekripsi Email dengan Vigenère Cipher

LockMail adalah aplikasi desktop berbasis Python dan Tkinter (menggunakan tema `ttkbootstrap`) yang memungkinkan pengguna untuk mengenkripsi dan mendekripsi pesan email menggunakan algoritma Vigenère cipher. Aplikasi ini dirancang untuk kemudahan penggunaan dengan antarmuka grafis yang intuitif.

---

## 🔧 Fitur Utama

- **Enkripsi Pesan:** Mengubah teks biasa menjadi teks terenkripsi menggunakan kunci tertentu.
- **Dekripsi Pesan:** Mengembalikan teks terenkripsi menjadi teks asli dengan kunci yang sama.
- **Clipboard Integration:** Hasil enkripsi atau dekripsi dapat langsung disalin ke clipboard.
- **UI Modern:** Menggunakan `ttkbootstrap` untuk tampilan antarmuka yang menarik dan modern.

---

## 🗂 Struktur Proyek

```
LockMail/
├── main.py                  # Entry point aplikasi GUI
├── vigenere.py             # Implementasi algoritma Vigenère cipher
├── clipboard_utils.py      # Utilitas untuk menyalin teks ke clipboard
├── tests/
│   └── test_vigenere.py    # Unit test untuk enkripsi dan dekripsi
└── README.md               # Dokumentasi aplikasi
```

---

## 🚀 Cara Menjalankan

### 1. Install Dependensi

```bash
pip install ttkbootstrap
```

### 2. Jalankan Aplikasi

```bash
python main.py
```

---

## 🧠 Penjelasan Fungsi Utama

### `generate_key(pesan: str, kunci: str) -> str`

Menghasilkan kunci dengan panjang yang sama dengan pesan. Jika kunci kosong, akan memicu `ValueError`.

### `enkripsi_vigenere(pesan: str, kunci: str) -> str`

Mengenkripsi pesan menggunakan Vigenère cipher. Memperhatikan huruf kapital dan kecil, serta mengabaikan karakter non-alfabet.

### `dekripsi_vigenere(pesan: str, kunci: str) -> str`

Mendekripsi pesan terenkripsi menjadi teks asli menggunakan Vigenère cipher.

---

## 🧪 Pengujian

### Menjalankan Tes

```bash
python tests/test_vigenere.py
```

### Cakupan Tes

- Enkripsi dan dekripsi dengan kunci yang valid
- Penanganan huruf kapital dan huruf kecil
- Penanganan karakter non-alfabet
- Kunci kosong (harus memunculkan `ValueError`)

---

## 📸 Tampilan Antarmuka

- **Tombol Enkripsi & Dekripsi** di jendela utama
- **Form Kunci** dan **Text Box Email** di masing-masing jendela
- **Tombol Submit** untuk memproses dan tombol **Cancel** untuk menutup jendela

---

## 👨‍💻 Kontributor

- Faisal Maulana
- Faza
- Colin

---

## 📃 Lisensi

Proyek ini adalah open-source dan bebas digunakan untuk pembelajaran pribadi.