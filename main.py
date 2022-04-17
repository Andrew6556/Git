import hashlib
import inspect



word_to_encrypt: str = input("Введите слово или фразу для шифрования\n")

print(inspect.cleandoc("""
        Каким способом зашифровать:
        1. MD5
        2. SHA1
        3. SHA2
    """))

choice_encryption: int = int(input('Введите способ шифрования(цифрой)\n'))

if choice_encryption == 1:
    hash_object = hashlib.md5(word_to_encrypt.encode())
elif choice_encryption == 2:
    hash_object = hashlib.sha1(word_to_encrypt.encode())
elif choice_encryption == 3:
    hash_object = hashlib.sha256(word_to_encrypt.encode())

print(f'Вот что получилось:\n{hash_object.hexdigest()}')