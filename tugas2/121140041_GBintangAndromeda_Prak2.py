# membuat class terlebih dahulu dengan huruf awal kapital
class Data:
    # membuat atribut objek nama, nim, kelasPBO, jumlahSKS, dan angkatan beserta construtornya
    def __init__(self, nama, nim, kelasPBO, jumlahSKS, angkatan):
        self.nama = nama
        self.nim = nim
        self.kelasPBO = kelasPBO
        self.jumlahSKS = jumlahSKS
        self.angkatan = angkatan
    
    # method untuk menampilkan data pada objek yang telah di instansiasi
    def menampilkanData(self):
        print("Nama : ", self.nama)
        print("NIM : ", self.nim)
        print("kelasPBO : ", self.kelasPBO)
        print("Jumlah SKS : ", self.jumlahSKS)
        print("angkatan : ", self.angkatan)

# proses instansiasi objek
dataSaya = Data("G.Bintang Andromeda", "121140041", "RB", 18 , 2021)

# output objek 
dataSaya.menampilkanData()
