# data password benar disimpan dalam variabel
username = "informatika"
password = "12345678"

# percobaan memasukkan password jika lebih dari 3 kali diblokir
for i in range(4):
    # inputan di casting ke tipe data string
    inputUsername = str(input("Enter your username : "))
    inputPassword = str(input("Enter your password : "))
    # percabangan logic untuk validasi login
    if inputUsername == username and inputPassword == password:
        print("Username anda : ", inputUsername)
        print("Password anda : ", inputPassword)
        print("Berhasil login!")
        exit()
    elif i==3 and (inputUsername != username or inputPassword != password):
        print("Akun diblokir")
    else: 
        print("Username atau password salah coba lagi\n")

    
        
