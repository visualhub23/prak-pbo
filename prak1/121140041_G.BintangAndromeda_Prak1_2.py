username = "informatika"
password = "12345678"


for i in range(4):
    inputUsername = str(input("Enter your username : "))
    inputPassword = str(input("Enter your password : "))
    
    if inputUsername == username and inputPassword == password:
        print("Username anda : ", inputUsername)
        print("Password anda : ", inputPassword)
        print("Berhasil login!")
        exit()
    elif i==3 and (inputUsername != username or inputPassword != password):
        print("Akun diblokir")
    else: 
        print("Username atau password salah coba lagi\n")

    
        
