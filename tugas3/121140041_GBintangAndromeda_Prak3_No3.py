# class Mahasiswa berisi data diri sederhana dari mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama, alamat_email):
        self.__nim = nim #private atribut h
        self._alamat_email = alamat_email #protected atribut
        self.nama = nama #public atribut
    
    # ===== SECTION PENGGUNAAN PRIVATE ATTRIBUTE =====
    # getter untuk mengakses private atribut nim yang hanya dapat diakses pada class level    
    # dengan menggunakan getter maka method ini akan menjadi read only, untuk itu membutuhkan setter untuk memanipulasi data tersebut
    @property
    def nim_mahasiswa(self):
        return self.__nim
    
    # setter untuk memanipulasi data yang telah diambil(get) oleh getter
    @nim_mahasiswa.setter
    def nim_mahasiswa(self,nim_baru):
        print(f"NIM anda : {self.__nim} berubah menjadi {nim_baru}")
        self.__nim = nim_baru
    # ===== AKHIR SECTION PENGGUNAAN PRIVATE ATTRIBUTE =====

# protected attribute dapat diakses pada class yang diheritance
class Child(Mahasiswa):
    def __init__(self):
        super().__init__()
        # mengakses protected attribut _alamat email dari child class/sub class
        print(self._alamat_email)
        
        
# instansiasi objek 
mhs1 = Mahasiswa("121140041","G.BintangAndromeda","androgba519@gmail.com")


# ====== acces private attribute ======
print(mhs1.nim_mahasiswa) #dari getter
mhs1.nim_mahasiswa = "12222222" #dari setter
# ====== akhir acces private attribute ======


# ====== acces protected attribute ======
print(mhs1._alamat_email)
# ====== akhir acces protected attribute ======

# ====== acces public attribute ======
mhs1.nama = "Jack Kahuna A" #attribute bisa dimanipulasi secara langsung pada level objek
print(mhs1.nama)
# ====== akhir acces public attribute ======


