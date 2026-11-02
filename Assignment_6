
import hashlib

text = input("Enter a text: ")

# Calculate SHA-1 digest
digest1 = hashlib.sha1(text.encode()).hexdigest()
print("SHA-1 Digest:", digest1)

# Change one character to demonstrate the effect
changed_text = text + "!"

digest2 = hashlib.sha1(changed_text.encode()).hexdigest()
print("Modified Text:", changed_text)
print("Modified Digest:", digest2)

if digest1 == digest2:
    print("Digests match")
else:
    print("Digests differ - input has changed")
