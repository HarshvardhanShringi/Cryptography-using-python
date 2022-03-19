from cryptography.fernet import Fernet
import tkinter
from tkinter import IntVar
from tkinter import font
from tkinter import filedialog


def openfile():
    global filepath
    filepath=filedialog.askopenfilename()
    g=tkinter.Label(m,text=filepath)
    g.pack()

def encryption():
    kfile_path=b'C:\Program Files\Dell\Update\key.txt'
    g = open(kfile_path, 'rb')
    k=g.read()
    token=Fernet(k)
    orig_file_path=filepath
    file = open(orig_file_path,'rb')
    orig_data = file.read()
    enc_data = token.encrypt(orig_data)
    file1 = open(orig_file_path, 'wb')
    file1.write(enc_data)

def decryption():
    kfile_path=b'C:\Program Files\Dell\Update\key.txt'
    g = open(kfile_path, 'rb')
    k=g.read()
    token=Fernet(k)
    dec_file_path=filepath
    file2= open(dec_file_path, 'rb')
    enc_data = file2.read()
    dec_data = token.decrypt(enc_data)
    file3 = open(dec_file_path, 'wb')
    file3.write(dec_data)

def isbutton_checked():
    e_text=namvar.get()
    if e_text=='hukumenc':
        encryption()
        t=tkinter.Label(m,text='encryption successfull',fg='green',font=("Courier", 30))
        t.pack(side='bottom')

    if e_text=='hukumdec':
        decryption()
        t1=tkinter.Label(m,text='decryption successfull',fg='green',font=("Courier", 30))
        t1.pack(side='bottom')

m=tkinter.Tk()
m.geometry('1600x1000')
m.title('practise')


but=tkinter.Button(m,activebackground='cyan',text='Start',command=isbutton_checked,width=14,height=1,font=15,bd=6,bg='white')
but.pack(side='bottom',pady=150)
but2=tkinter.Button(m,activebackground='cyan',command=openfile,text='select file',width=14,height=1,font=10,bd=2,bg='white')
but2.pack(side='top',pady=60,padx=30)

namvar=tkinter.StringVar()
entry=tkinter.Entry(m,width=30,textvariable=namvar,bg='white',show='*')
entry.pack(side='bottom',pady=30)

m.mainloop()
