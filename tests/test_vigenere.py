import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import vigenere

class TestLockMail(unittest.TestCase):

    def test_enkripsi_dekripsi(self):
        plaintext = "Halo, ini adalah email penting."
        key = "RAHASIA"

        encrypted = vigenere.enkripsi_vigenere(plaintext, key)
        decrypted = vigenere.dekripsi_vigenere(encrypted, key)

        self.assertNotEqual(encrypted, plaintext, "Teks terenkripsi harus berbeda dari plaintext")
        self.assertEqual(decrypted, plaintext, "Hasil dekripsi harus sama dengan plaintext asli")

    def test_enkripsi_case_insensitive(self):
        plaintext = "Email Sama"
        key1 = "KUNCI"
        key2 = "kunci"

        enc1 = vigenere.enkripsi_vigenere(plaintext, key1)
        enc2 = vigenere.enkripsi_vigenere(plaintext, key2)

        self.assertEqual(enc1, enc2, "Enkripsi harus case-insensitive untuk kunci")

    def test_empty_plaintext(self):
        plaintext = ""
        key = "RAHASIA"
        encrypted = vigenere.enkripsi_vigenere(plaintext, key)
        decrypted = vigenere.dekripsi_vigenere(encrypted, key)

        self.assertEqual(encrypted, "")
        self.assertEqual(decrypted, "")

    def test_empty_key(self):
        plaintext = "Tes Email"
        key = ""

        with self.assertRaises(ValueError):
            vigenere.enkripsi_vigenere(plaintext, key)

        with self.assertRaises(ValueError):
            vigenere.dekripsi_vigenere(plaintext, key)

if __name__ == '__main__':
    unittest.main()
