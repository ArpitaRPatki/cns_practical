
import time
import secrets
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


for size in [1024, 2048, 3072]:

    # Key generation time
    start = time.perf_counter()
    private = rsa.generate_private_key(
        public_exponent=65537, key_size=size
    )
    public = private.public_key()
    key_time = time.perf_counter() - start

    print("\nRSA Key Size:", size, "bits")
    print("Key Generation:", round(key_time, 6), "seconds")

    for n in [64, 128, 256]:
        message = secrets.token_bytes(n // 8)

        # Encryption time
        start = time.perf_counter()
        for _ in range(5):
            cipher = public.encrypt(
                message,
                padding.OAEP(
                    mgf=padding.MGF1(hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        enc_time = (time.perf_counter() - start) / 5

        # Decryption time
        start = time.perf_counter()
        for _ in range(5):
            plain = private.decrypt(
                cipher,
                padding.OAEP(
                    mgf=padding.MGF1(hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        dec_time = (time.perf_counter() - start) / 5

        print("\nMessage Size:", n, "bits")
        print("Encryption:", round(enc_time, 6), "seconds")
        print("Decryption:", round(dec_time, 6), "seconds")
        print("Correct:", plain == message)
