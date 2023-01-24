import hashlib
import itertools
import time

# Set the target hash
target_hash = input("Passord-hash\n")

# Define the characters to use in the brute force
characters = "abcdefghijklmnopqrstuvwxyz0123456789"

# Define the maximum length of the plaintext string
max_length = 8

# Define the number of rounds to apply the hash function
rounds = int(input("Antall iterasjoner\n"))

start = time.perf_counter()
# Iterate over all possible plaintext strings of length 1 to max_length
for length in range(1, max_length + 1):
    for plaintext in itertools.product(characters, repeat=length):
        plaintext = "".join(plaintext)
        hash_value = plaintext
        print(plaintext)
        # Apply the hash function multiple times
        for _ in range(rounds):
            hash_value = hashlib.sha1(hash_value.encode()).hexdigest()
        #hash_value = hash_value.hex()

        # Check if the hash matches the target
        if hash_value == target_hash:
            print(f"Found plaintext: {plaintext}")
            stop = time.perf_counter()
            print(f"Tid: {stop - start:0.4}")
            exit()


print("Plaintext not found.")
