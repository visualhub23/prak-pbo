class AkunBank:
    list_pelanggan = []
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
    
    # Aksi ketika satu objek sudah diisntansiasi, akan menambahkan objek di akhir list 
        AkunBank.list_pelanggan.append(self)
    
    # method tampilan menu 
    def lihat_menu():
        print("Selamat datang di Bank Jago")
        print("Halo nama_kalian, ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")     
        print("3. Transfer saldo")       
        print("4. Keluar")        
        print("*Note: Masukkan inputan berupa angka!")        
    
    # untuk menampilkan list objek yang di simpan didalam list_pelanggan, sumber refrensi "freeCodeCamp oop python" 
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__no_pelanggan}', {self.__nama_pelanggan}, {self.__jumlah_saldo}"
    
    def lihat_saldo(self):
        return f"{self.__nama_pelanggan} memiliki saldo Rp{self.__jumlah_saldo}" 
    
    def tarik_tunai(self):
        # akan terus melakukan loop jika inputan amount pengguna tidak valid
        while True:
            amount = input("Jumlah penarikan? Rp")
            # cek apakah inputan yang dimasukan merupakan (valid number) angka dan angka tersebut positif, karna jika tidak begitu maka bisa dimasukkan apa saja
            if amount.isdigit():
                # casting ke integer
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("Jumlah penarikan harus lebih dari Rp0.")
            else:
                print("Masukan harus berupa angka positif.")
        self.__jumlah_saldo -= amount
        return self.__jumlah_saldo

    def transfer(self):
    # akan terus melakukan loop jika inputan amount pengguna tidak valid
        while True:
            amount = input("Nominal transfer? Rp")
            no_rekening = input("Masukkan no rekening tujuan : ")
            # cek apakah inputan yang dimasukan merupakan (valid number) angka dan angka tersebut positif, karna jika tidak begitu maka bisa dimasukkan apa saja
            if amount.isdigit() and no_rekening.isdigit():
                # casting ke integer
                amount = int(amount)
                no_rekening = int(no_rekening)
                if amount > 0:
                    if no_rekening == Akun2.__no_pelanggan:
                        Akun2.__jumlah_saldo += amount
                        print(Akun2.lihat_saldo())
                        break
                    elif no_rekening == Akun3.__no_pelanggan:
                        Akun3.__jumlah_saldo += amount
                        print(Akun3.lihat_saldo())
                        break
                    else:
                        print("No rekening tidak ditemukan")
                else:
                    print("Jumlah penarikan harus lebih dari Rp0.")
            else:
                print("Masukan harus berupa angka positif.")
        

# instansiasi objek
# Note : Akun1 = Akun saya
Akun1 = AkunBank(1234, "Andromeda", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 10000)
Akun3 = AkunBank(3456, "Elon Musk", 20000)

AkunBank.lihat_menu()

while True:
    print("")
    input_pengguna = str(input("Masukkan nomor input: "))
    if input_pengguna == "1":
        print(Akun1.lihat_saldo())
    elif input_pengguna == "2":
        Akun1.tarik_tunai()
        print(Akun1.lihat_saldo())
    elif input_pengguna == "3":
        Akun1.transfer()
    elif input_pengguna == "4":
        break
    else:
        print("Allert : Silahkan masukkan nomor input sesuai nomor pilihan pada menu!")


