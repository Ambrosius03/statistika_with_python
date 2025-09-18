import math # Import pustaka math untuk fungsi matematika
import numpy as np # Import pustaka numpy untuk operasi numerik
import matplotlib.pyplot as plt # Import pustaka matplotlib untuk membuat plot

class DataAnalyzer: # Definisikan kelas DataAnalyzer
    def __init__(self, data): # Metode inisialisasi kelas
        self.data = data # Simpan data yang diberikan
        self.N = len(data) # Hitung jumlah data
        self.X = max(data) # Cari nilai terbesar dalam data
        self.Y = min(data) # Cari nilai terkecil dalam data
        self.R = self.X - self.Y # Hitung rentang data
        self.k = self.sturges_rule() # Hitung jumlah kelas menggunakan aturan Sturges
        self.Z = self.R / self.k # Hitung panjang kelas sementara
        self.h = math.ceil(self.Z) # Bulatkan panjang kelas ke atas
        self.kelas = self.determine_classes() # Tentukan batas-batas kelas
        self.frekuensi = self.calculate_frequency() # Hitung frekuensi setiap kelas
        self.frekuensi_relatif = self.calculate_relative_frequency() # Hitung frekuensi relatif setiap kelas
        self.frekuensi_kumulatif = self.calculate_cumulative_frequency() # Hitung frekuensi kumulatif setiap kelas
        self.mean_data = np.mean(data) # Hitung rata-rata data
        self.median_data = np.median(data) # Hitung median data
        self.std_dev_data = np.std(data) # Hitung standar deviasi data


    def sturges_rule(self): # Metode untuk menghitung jumlah kelas menggunakan aturan Sturges
        if self.N <= 0: # Jika jumlah data kurang dari atau sama dengan 0
            return 0 # Kembalikan 0
        else: # Jika jumlah data lebih dari 0
            k = 1 + 3.3 * math.log10(self.N) # Hitung jumlah kelas menggunakan rumus Sturges
            return round(k) # Bulatkan jumlah kelas ke bilangan bulat terdekat

    def determine_classes(self): # Metode untuk menentukan batas-batas kelas
        start = (self.Y // self.h) * self.h # Tentukan titik awal batas bawah kelas pertama
        kelas = [] # Buat list kosong untuk menyimpan batas kelas
        for i in range(self.k): # Lakukan iterasi sebanyak jumlah kelas
            lower = start + i * self.h # Hitung batas bawah kelas
            upper = start + (i + 1) * self.h - 1 # Hitung batas atas kelas (dikurangi 1 untuk menghindari tumpang tindih)
            kelas.append((lower, upper)) # Tambahkan tuple batas bawah dan atas ke list kelas
        return kelas # Kembalikan list batas kelas

    def calculate_frequency(self): # Metode untuk menghitung frekuensi setiap kelas
        frekuensi = [] # Buat list kosong untuk menyimpan frekuensi
        for lower, upper in self.kelas: # Lakukan iterasi melalui setiap batas kelas
            count = sum(1 for x in self.data if lower <= x <= upper) # Hitung jumlah data dalam rentang kelas
            frekuensi.append((lower, upper, count)) # Tambahkan tuple batas bawah, atas, dan frekuensi ke list frekuensi
        return frekuensi # Kembalikan list frekuensi

    def calculate_relative_frequency(self): # Metode untuk menghitung frekuensi relatif setiap kelas
        frekuensi_relatif = [] # Buat list kosong untuk menyimpan frekuensi relatif
        for lower, upper, count in self.frekuensi: # Lakukan iterasi melalui setiap entri frekuensi
            frekuensi_relatif.append((lower, upper, count, (count / self.N) * 100)) # Hitung frekuensi relatif (dalam persen) dan tambahkan ke list
        return frekuensi_relatif # Kembalikan list frekuensi relatif

    def calculate_cumulative_frequency(self): # Metode untuk menghitung frekuensi kumulatif setiap kelas
        frekuensi_kumulatif = [] # Buat list kosong untuk menyimpan frekuensi kumulatif
        total = 0 # Inisialisasi total frekuensi kumulatif
        for lower, upper, count in self.frekuensi: # Lakukan iterasi melalui setiap entri frekuensi
            total += count # Tambahkan frekuensi saat ini ke total
            frekuensi_kumulatif.append((lower, upper, total)) # Tambahkan tuple batas bawah, atas, dan total kumulatif ke list
        return frekuensi_kumulatif # Kembalikan list frekuensi kumulatif

    def plot_histogram(self): # Metode untuk membuat histogram
        plt.hist(self.data, bins=self.k, edgecolor='black') # Buat histogram dengan data, jumlah kelas, dan tepi batang hitam
        plt.xlabel('Nilai') # Atur label sumbu x
        plt.ylabel('Frekuensi') # Atur label sumbu y
        plt.title('Histogram Data') # Atur judul histogram
        plt.show() # Tampilkan histogram

    def print_summary(self): # Metode untuk mencetak ringkasan analisis data
        print("Summary Data Analysis:") # Cetak judul ringkasan
        print(f"Jumlah Data (N): {self.N}") # Cetak jumlah data
        print(f"Nilai Terbesar (X): {self.X}") # Cetak nilai terbesar
        print(f"Nilai Terkecil (Y): {self.Y}") # Cetak nilai terkecil
        print(f"Rentang (R): {self.R}") # Cetak rentang
        print(f"Jumlah Kelas (k): {self.k}") # Cetak jumlah kelas
        print(f"Panjang Kelas (h): {self.h}") # Cetak panjang kelas
        print("\nBatas Kelas:") # Cetak judul batas kelas
        for k in self.kelas: # Lakukan iterasi melalui setiap batas kelas
            print(k) # Cetak batas kelas
        print("\nDistribusi Frekuensi (Kelas, Frekuensi, Frekuensi Relatif):") # Cetak judul distribusi frekuensi
        for fr in self.frekuensi_relatif: # Lakukan iterasi melalui setiap entri frekuensi relatif
            print(f"Kelas: {fr[0]}-{fr[1]}, Frekuensi: {fr[2]}, Frekuensi Relatif: {fr[3]:.2f}%") # Cetak kelas, frekuensi, dan frekuensi relatif
        print("\nFrekuensi Kumulatif:") # Cetak judul frekuensi kumulatif
        for fk in self.frekuensi_kumulatif: # Lakukan iterasi melalui setiap entri frekuensi kumulatif
            print(f"Kelas: {fk[0]}-{fk[1]}, Frekuensi Kumulatif: {fk[2]}") # Cetak kelas dan frekuensi kumulatif
        print("\nStatistik Deskriptif:") # Cetak judul statistik deskriptif
        print(f"Rata-rata (Mean): {self.mean_data:.2f}") # Cetak rata-rata
        print(f"Median: {self.median_data:.2f}") # Cetak median
        print(f"Standar Deviasi: {self.std_dev_data:.2f}") # Cetak standar deviasi
