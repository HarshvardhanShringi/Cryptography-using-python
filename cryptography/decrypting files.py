# Initializing key
key='36HCIgIzZHAudc2gEvj0EB3min-4kmSwgxQjRqEmdMs='

# Creating token
ktoken=Fernet(key1)

# Reading file and storing encrypted data to a variable (enc_data)
gp=open('E:\Honey\Projects\Projects.txt','rb')
enc_data=gp.read()

# Decrypting data and storing it to another variable (dec_data)
dec_data=k1token.decrypt(cnt)

# Writing dec_data to that file
gp1=open('E:\Honey\Projects\Projects.txt','wb')
gp1.write(dec_data)
