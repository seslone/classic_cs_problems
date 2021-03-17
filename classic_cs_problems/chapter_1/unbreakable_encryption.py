from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    # generate lenth random bytes
    tb: bytes = token_bytes(length)
    # retun the bytes converted to a bit string
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes(
        (decrypted.bit_length() + 7) // 8, "big"
    )  # adding 7 circumvents any obo errors
    return temp.decode()


key1, key2 = encrypt("Hello World")
print("key1 = " + str(key1))
print("key2 = " + str(key2))
result = decrypt(key1, key2)
print(result)
