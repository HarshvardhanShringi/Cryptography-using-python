from cryptography.fernet import Fernet
key=Fernet.generate_key()
token=Fernet(key)
encrypted_text=token.encrypt(b"happy new year")
#print(cipher_text)
#print(key)
decrypted_text=token.decrypt(encrypted_text)
print(decrypted_text)
