from cryptography.fernet import Fernet
key=Fernet.generate_key()
data='hey welcome'
token=Fernet(key)
encrypted_text=token.encrypt(data.encode())
decrypted_text=token.decrypt(encrypted_text)
print(encrypted_text)
print(key)
print(decrypted_text)
