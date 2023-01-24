import hashlib
import itertools

# Set the target hash
target_hash = input('Passord-hash\n')

# Define the characters to use in the brute force
characters = "abcdefghijklmnopqrstuvwxyz0123456789"

# Define the maximum length of the plaintext string
max_length = 8

# Iterate over all possible plaintext strings of length 1 to max_length
for length in range(1, max_length + 1):
    for plaintext in itertools.product(characters, repeat=length):
        plaintext = "".join(plaintext)
        print(plaintext)
        hash_value = hashlib.sha1(plaintext.encode()).hexdigest()

        # Check if the hash matches the target
        if hash_value == target_hash:
            print(f"Found plaintext: {plaintext}")
            exit()

print("Plaintext not found.")
