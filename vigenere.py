def generate_key(pesan, kunci):
    if not kunci:
        raise ValueError("Kunci tidak boleh kosong.")
    
    kunci = kunci.upper()  # Biar case-insensitive
    kunci = list(kunci)
    
    if len(pesan) == len(kunci):
        return kunci
    else:
        for i in range(len(pesan) - len(kunci)):
            kunci.append(kunci[i % len(kunci)])
    
    return "".join(kunci)

def enkripsi_vigenere(pesan, kunci):
    if not kunci:
        raise ValueError("Kunci tidak boleh kosong.")
    
    kunci = generate_key(pesan, kunci)
    pesan_enkripsi = []

    for i in range(len(pesan)):
        char = pesan[i]
        k = kunci[i]

        if char.isupper():
            enkripsi_char = chr((ord(char) + ord(k.upper()) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            enkripsi_char = chr((ord(char) + ord(k.lower()) - 2 * ord('a')) % 26 + ord('a'))
        else:
            enkripsi_char = char
        pesan_enkripsi.append(enkripsi_char)

    return "".join(pesan_enkripsi)

def dekripsi_vigenere(pesan, kunci):
    if not kunci:
        raise ValueError("Kunci tidak boleh kosong.")
    
    kunci = generate_key(pesan, kunci)
    pesan_dekripsi = []

    for i in range(len(pesan)):
        char = pesan[i]
        k = kunci[i]

        if char.isupper():
            dekripsi_char = chr((ord(char) - ord(k.upper()) + 26) % 26 + ord('A'))
        elif char.islower():
            dekripsi_char = chr((ord(char) - ord(k.lower()) + 26) % 26 + ord('a'))
        else:
            dekripsi_char = char
        pesan_dekripsi.append(dekripsi_char)

    return "".join(pesan_dekripsi)
