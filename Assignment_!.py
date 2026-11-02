
# import math
# import string


# # --------------------------------------------------
# # 1. CAESAR CIPHER
# # --------------------------------------------------

# def caesar_encrypt(text, key):
#     result = ""
#     for ch in text:
#         if ch.isalpha():
#             base = ord('A') if ch.isupper() else ord('a')
#             result += chr((ord(ch) - base + key) % 26 + base)
#         else:
#             result += ch
#     return result


# def caesar_decrypt(text, key):
#     return caesar_encrypt(text, -key)


# # --------------------------------------------------
# # 2. PLAYFAIR CIPHER
# # --------------------------------------------------

# def create_playfair_matrix(key):
#     key = key.upper().replace("J", "I")
#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
#     chars = []

#     for ch in key + alphabet:
#         if ch.isalpha() and ch not in chars:
#             chars.append(ch)

#     return [chars[i:i + 5] for i in range(0, 25, 5)]


# def playfair_prepare(text):
#     text = "".join(ch for ch in text.upper() if ch.isalpha())
#     text = text.replace("J", "I")
#     pairs = []
#     i = 0

#     while i < len(text):
#         a = text[i]

#         if i + 1 >= len(text):
#             b = "X" if a != "X" else "Q"
#             i += 1
#         elif text[i + 1] == a:
#             b = "X" if a != "X" else "Q"
#             i += 1
#         else:
#             b = text[i + 1]
#             i += 2

#         pairs.append(a + b)

#     return pairs


# def playfair_transform(text, key, decrypt=False):
#     matrix = create_playfair_matrix(key)
#     pairs = playfair_prepare(text) if not decrypt else [
#         text.upper().replace("J", "I")[i:i + 2]
#         for i in range(0, len(text), 2)
#         if len(text[i:i + 2]) == 2
#     ]

#     result = ""

#     for pair in pairs:
#         a, b = pair
#         r1, c1 = next(
#             (r, c) for r in range(5) for c in range(5)
#             if matrix[r][c] == a
#         )
#         r2, c2 = next(
#             (r, c) for r in range(5) for c in range(5)
#             if matrix[r][c] == b
#         )

#         shift = -1 if decrypt else 1

#         if r1 == r2:
#             result += matrix[r1][(c1 + shift) % 5]
#             result += matrix[r2][(c2 + shift) % 5]
#         elif c1 == c2:
#             result += matrix[(r1 + shift) % 5][c1]
#             result += matrix[(r2 + shift) % 5][c2]
#         else:
#             result += matrix[r1][c2]
#             result += matrix[r2][c1]

#     return result


# def playfair_encrypt(text, key):
#     return playfair_transform(text, key)


# def playfair_decrypt(text, key):
#     return playfair_transform(text, key, decrypt=True)


# # --------------------------------------------------
# # 3. VIGENERE CIPHER
# # --------------------------------------------------

# def vigenere_cipher(text, key, decrypt=False):
#     key = "".join(ch.upper() for ch in key if ch.isalpha())

#     if not key:
#         raise ValueError("Key must contain at least one letter.")

#     result = ""
#     key_index = 0
#     direction = -1 if decrypt else 1

#     for ch in text:
#         if ch.isalpha():
#             base = ord('A') if ch.isupper() else ord('a')
#             shift = ord(key[key_index % len(key)]) - ord('A')
#             result += chr(
#                 (ord(ch) - base + direction * shift) % 26 + base
#             )
#             key_index += 1
#         else:
#             result += ch

#     return result


# # --------------------------------------------------
# # 4. RAIL FENCE CIPHER
# # --------------------------------------------------

# def rail_fence_encrypt(text, rails):
#     if rails < 2:
#         raise ValueError("Number of rails must be at least 2.")

#     fence = [""] * rails
#     row = 0
#     direction = 1

#     for ch in text:
#         fence[row] += ch

#         if row == 0:
#             direction = 1
#         elif row == rails - 1:
#             direction = -1

#         row += direction

#     return "".join(fence)


# def rail_fence_decrypt(ciphertext, rails):
#     if rails < 2:
#         raise ValueError("Number of rails must be at least 2.")

#     n = len(ciphertext)
#     pattern = []
#     row = 0
#     direction = 1

#     for _ in range(n):
#         pattern.append(row)

#         if row == 0:
#             direction = 1
#         elif row == rails - 1:
#             direction = -1

#         row += direction

#     counts = [pattern.count(r) for r in range(rails)]
#     fence = []
#     pos = 0

#     for count in counts:
#         fence.append(list(ciphertext[pos:pos + count]))
#         pos += count

#     indices = [0] * rails
#     result = ""

#     for r in pattern:
#         result += fence[r][indices[r]]
#         indices[r] += 1

#     return result


# # --------------------------------------------------
# # 5. ROW & COLUMN TRANSPOSITION CIPHER
# #    Uses a keyword to determine column order.
# # --------------------------------------------------

# def column_order(key):
#     return sorted(range(len(key)), key=lambda i: (key[i], i))


# def row_column_encrypt(text, key):
#     key = key.upper()

#     if not key.isalpha():
#         raise ValueError("Key must contain letters only.")

#     cols = len(key)
#     rows = math.ceil(len(text) / cols)
#     padded = text.ljust(rows * cols, "X")

#     matrix = [
#         padded[i:i + cols]
#         for i in range(0, len(padded), cols)
#     ]

#     result = ""

#     for c in column_order(key):
#         for r in range(rows):
#             result += matrix[r][c]

#     return result


# def row_column_decrypt(ciphertext, key):
#     key = key.upper()

#     if not key.isalpha():
#         raise ValueError("Key must contain letters only.")

#     cols = len(key)
#     rows = math.ceil(len(ciphertext) / cols)

#     if len(ciphertext) % cols != 0:
#         raise ValueError("Invalid ciphertext length.")

#     matrix = [[""] * cols for _ in range(rows)]
#     pos = 0

#     for c in column_order(key):
#         for r in range(rows):
#             matrix[r][c] = ciphertext[pos]
#             pos += 1

#     result = "".join("".join(row) for row in matrix)
#     return result.rstrip("X")


# # --------------------------------------------------
# # MAIN MENU
# # --------------------------------------------------

# def main():
#     while True:
#         print("\n===== CLASSICAL ENCRYPTION TECHNIQUES =====")
#         print("1. Caesar Cipher")
#         print("2. Playfair Cipher")
#         print("3. Vigenere Cipher")
#         print("4. Rail Fence Cipher")
#         print("5. Row & Column Transposition Cipher")
#         print("6. Exit")

#         choice = input("Enter your choice (1-6): ")

#         if choice == "6":
#             print("Program terminated.")
#             break

#         if choice not in ("1", "2", "3", "4", "5"):
#             print("Invalid choice. Try again.")
#             continue

#         text = input("Enter the text: ")

#         try:
#             if choice == "1":
#                 key = int(input("Enter shift key (number): "))
#                 mode = input("Encrypt or Decrypt (E/D): ").upper()

#                 if mode == "E":
#                     result = caesar_encrypt(text, key)
#                 elif mode == "D":
#                     result = caesar_decrypt(text, key)
#                 else:
#                     print("Invalid operation.")
#                     continue

#             elif choice == "2":
#                 key = input("Enter keyword: ")
#                 mode = input("Encrypt or Decrypt (E/D): ").upper()

#                 if mode == "E":
#                     result = playfair_encrypt(text, key)
#                 elif mode == "D":
#                     result = playfair_decrypt(text, key)
#                 else:
#                     print("Invalid operation.")
#                     continue

#             elif choice == "3":
#                 key = input("Enter keyword: ")
#                 mode = input("Encrypt or Decrypt (E/D): ").upper()

#                 if mode == "E":
#                     result = vigenere_cipher(text, key)
#                 elif mode == "D":
#                     result = vigenere_cipher(text, key, decrypt=True)
#                 else:
#                     print("Invalid operation.")
#                     continue

#             elif choice == "4":
#                 key = int(input("Enter number of rails: "))
#                 mode = input("Encrypt or Decrypt (E/D): ").upper()

#                 if mode == "E":
#                     result = rail_fence_encrypt(text, key)
#                 elif mode == "D":
#                     result = rail_fence_decrypt(text, key)
#                 else:
#                     print("Invalid operation.")
#                     continue

#             else:
#                 key = input("Enter column keyword: ")
#                 mode = input("Encrypt or Decrypt (E/D): ").upper()

#                 if mode == "E":
#                     result = row_column_encrypt(text, key)
#                 elif mode == "D":
#                     result = row_column_decrypt(text, key)
#                 else:
#                     print("Invalid operation.")
#                     continue

#             print("Result:", result)

#         except ValueError as error:
#             print("Error:", error)


# if __name__ == "__main__":
#     main()


# 1. Caesar Cipher
def caesar(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result


# 2. Playfair Cipher
def playfair(text, key, decrypt=False):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")
    matrix_text = ""

    for ch in key + alphabet:
        if ch.isalpha() and ch != "J" and ch not in matrix_text:
            matrix_text += ch

    matrix = [matrix_text[i:i+5] for i in range(0, 25, 5)]
    text = "".join(c for c in text.upper() if c.isalpha())
    text = text.replace("J", "I")

    pairs = []
    if decrypt:
        if len(text) % 2:
            raise ValueError("Ciphertext length must be even.")
        pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    else:
        i = 0
        while i < len(text):
            a = text[i]
            if i + 1 == len(text):
                b = "X" if a != "X" else "Q"
                i += 1
            elif text[i] == text[i+1]:
                b = "X" if a != "X" else "Q"
                i += 1
            else:
                b = text[i+1]
                i += 2
            pairs.append(a + b)

    result = ""
    shift = -1 if decrypt else 1

    for a, b in pairs:
        r1, c1 = next((r, c) for r in range(5)
                      for c in range(5) if matrix[r][c] == a)
        r2, c2 = next((r, c) for r in range(5)
                      for c in range(5) if matrix[r][c] == b)

        if r1 == r2:
            result += matrix[r1][(c1 + shift) % 5]
            result += matrix[r2][(c2 + shift) % 5]
        elif c1 == c2:
            result += matrix[(r1 + shift) % 5][c1]
            result += matrix[(r2 + shift) % 5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]

    return result


# 3. Vigenere Cipher
def vigenere(text, key, decrypt=False):
    key = key.upper()
    result = ""
    j = 0
    shift = -1 if decrypt else 1

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            k = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(ch) - base + shift*k) % 26 + base)
            j += 1
        else:
            result += ch
    return result


# 4. Rail Fence Cipher
def rail_fence(text, rails, decrypt=False):
    if rails < 2:
        raise ValueError("Rails must be at least 2.")

    pattern = []
    row, direction = 0, 1

    for _ in text:
        pattern.append(row)
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    if not decrypt:
        return "".join(text[i] for r in range(rails)
                       for i in range(len(text)) if pattern[i] == r)

    rows = [list(text[pattern.count(r) * 0:
                      pattern.count(r)]) for r in range(rails)]
    pos = 0
    for r in range(rails):
        count = pattern.count(r)
        rows[r] = list(text[pos:pos+count])
        pos += count

    result = ""
    for r in pattern:
        result += rows[r].pop(0)
    return result


# 5. Row and Column Transposition
def column_cipher(text, key, decrypt=False):
    if not key.isalpha():
        raise ValueError("Key must contain letters only.")

    if not decrypt:
        cols = len(key)
        pad = (-len(text)) % cols
        text += "X" * pad
        rows = [text[i:i+cols] for i in range(0, len(text), cols)]

        result = ""
        for c in sorted(range(cols), key=lambda i: (key[i], i)):
            for row in rows:
                result += row[c]

        return result + "|" + str(pad)

    text, pad = text.rsplit("|", 1)
    pad = int(pad)
    cols = len(key)
    rows = len(text) // cols
    matrix = [[""] * cols for _ in range(rows)]
    pos = 0

    for c in sorted(range(cols), key=lambda i: (key[i], i)):
        for r in range(rows):
            matrix[r][c] = text[pos]
            pos += 1

    return "".join("".join(row) for row in matrix)[:-pad] if pad else \
           "".join("".join(row) for row in matrix)


# Main menu
while True:
    print("\n1.Caesar  2.Playfair  3.Vigenere")
    print("4.Rail Fence  5.Row-Column  6.Exit")
    choice = input("Choice: ")

    if choice == "6":
        break

    text = input("Enter text: ")
    mode = input("Encrypt or Decrypt (E/D): ").upper()
    dec = mode == "D"

    if choice == "1":
        key = int(input("Shift key: "))
        print(caesar(text, -key if dec else key))

    elif choice == "2":
        key = input("Keyword: ")
        print(playfair(text, key, dec))

    elif choice == "3":
        key = input("Keyword: ")
        if not key.isalpha():
            print("Keyword must contain letters.")
            continue
        print(vigenere(text, key, dec))

    elif choice == "4":
        key = int(input("Number of rails: "))
        print(rail_fence(text, key, dec))

    elif choice == "5":
        key = input("Column keyword: ")
        print(column_cipher(text, key, dec))

    else:
        print("Invalid choice")
