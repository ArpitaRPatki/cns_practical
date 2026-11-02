
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Generate DSA keys
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

# Input message
message = input("Enter message: ").encode()

# Sign message using private key
signature = private_key.sign(
    message,
    hashes.SHA256()
)

print("\nDigital Signature:", signature.hex())

# Verify signature using public key
try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )
    print("Signature is valid.")
    print("Authentication and integrity verified.")

except Exception:
    print("Signature is invalid.")

# Test whether modification is detected
modified_message = message + b"!"
print("\nVerifying modified message:")

try:
    public_key.verify(
        signature,
        modified_message,
        hashes.SHA256()
    )
    print("Signature is valid.")
except Exception:
    print("Signature is invalid. Message was modified.")
