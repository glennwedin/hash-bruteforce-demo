import hashlib
import time
import binascii

password = input("Passord:\n")
rounds = int(input("Antall iterasjoner:\n"))
salt = input("Salt:\n")
password = password.encode('utf-8')

start = time.perf_counter()
result = ""
result = hashlib.pbkdf2_hmac("sha1", result.encode(
    "utf-8"), salt.encode("utf-8"), rounds)
result = binascii.hexlify(result).decode()
stop = time.perf_counter()


print(result)
print(f"Tid: {stop - start:0.4}")
