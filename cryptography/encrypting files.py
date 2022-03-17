#    1. importing fernet
from cryptography.fernet import Fernet

#    2. creating key, token and storing key into a txt file

key=Fernet.generate_key()
ktoken=Fernet(key)
g=open('E:\Honey\Projects\key.txt','wb')
g.write(key)

#    3. reading the orignal data from file

file=open('E:\Honey\Projects\Projects.txt','rb')
orig_data=file.read()

#    4. storing encrypted data into a variable

enc_data=ktoken.encrypt(orig_data)

#    5. writing that vairable (encrypted data) in the file

file1=open('E:\Honey\Projects\Projects.txt','wb')
file1.write(enc_data)


                   ########      files can be of any format       ########33
