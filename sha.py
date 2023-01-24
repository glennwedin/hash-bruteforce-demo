import hashlib
import time

password = input("Passord\n")
rounds = int(input("Antall iterasjoner\n"))
password = password.encode('utf-8')

start = time.perf_counter()
result = hashlib.sha1(password).hexdigest()
if rounds > 1:
    for length in range(1, rounds):
        result = hashlib.sha1(result.encode("utf-8")).hexdigest()
stop = time.perf_counter()


print(result)
print(f"Tid: {stop - start:0.4}")
