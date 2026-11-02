
# Custom Encryption and Decryption Algorithm

def encrypt(text, key):
    result = ""

    for i in range(len(text)):
        # XOR each character with a repeating key character
        value = ord(text[i]) ^ ord(key[i % len(key)])
        result += format(value, '02x')

    return result


def decrypt(cipher, key):
    result = ""

    # Read two hexadecimal characters at a time
    for i in range(0, len(cipher), 2):
        value = int(cipher[i:i + 2], 16)
        ch = chr(value ^ ord(key[(i // 2) % len(key)]))
        result += ch

    return result


# Main program
text = input("Enter plaintext: ")
key = input("Enter secret key: ")

if not key:
    print("Key cannot be empty!")
else:
    cipher = encrypt(text, key)
    print("Encrypted text:", cipher)

    original = decrypt(cipher, key)
    print("Decrypted text:", original)
