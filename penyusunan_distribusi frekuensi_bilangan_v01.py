import math
import numpy as np
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, data):
        self.data = data
        self.N = len(data)
        self.X = max(data)
        self.Y = min(data)
        self.R = self.X - self.Y
        self.k = self.sturges_rule()
        self.Z = self.R / self.k
        self.h = math.ceil(self.Z)
        self.kelas = self.determine_classes()
        self.frekuensi = self.calculate_frequency()
        self.frekuensi_relatif = self.calculate_relative_frequency()
        self.frekuensi_kumulatif = self.calculate_cumulative_frequency()
        self.mean_data = np.mean(data)
        self.median_data = np.median(data)
        self.std_dev_data = np.std(data)


    def sturges_rule(self):
        if self.N <= 0:
            return 0
        else:
            k = 1 + 3.3 * math.log10(self.N)
            return round(k)

    def determine_classes(self):
        start = (self.Y // self.h) * self.h
        kelas = []
        for i in range(self.k):
            lower = start + i * self.h
            upper = start + (i + 1) * self.h - 1
            kelas.append((lower, upper))
        return kelas

    def calculate_frequency(self):
        frekuensi = []
        for lower, upper in self.kelas:
            count = sum(1 for x in self.data if lower <= x <= upper)
            frekuensi.append((lower, upper, count))
        return frekuensi

    def calculate_relative_frequency(self):
        frekuensi_relatif = []
        for lower, upper, count in self.frekuensi:
            frekuensi_relatif.append((lower, upper, count, (count / self.N) * 100))
        return frekuensi_relatif

    def calculate_cumulative_frequency(self):
        frekuensi_kumulatif = []
        total = 0
        for lower, upper, count in self.frekuensi:
            total += count
            frekuensi_kumulatif.append((lower, upper, total))
        return frekuensi_kumulatif

    def plot_histogram(self):
        plt.hist(self.data, bins=self.k, edgecolor='black')
        plt.xlabel('Nilai')
        plt.ylabel('Frekuensi')
        plt.title('Histogram Data')
        plt.show()

    def print_summary(self):
        print("Summary Data Analysis:")
        print(f"Jumlah Data (N): {self.N}")
        print(f"Nilai Terbesar (X): {self.X}")
        print(f"Nilai Terkecil (Y): {self.Y}")
        print(f"Rentang (R): {self.R}")
        print(f"Jumlah Kelas (k): {self.k}")
        print(f"Panjang Kelas (h): {self.h}")
        print("\nBatas Kelas:")
        for k in self.kelas:
            print(k)
        print("\nDistribusi Frekuensi (Kelas, Frekuensi, Frekuensi Relatif):")
        for fr in self.frekuensi_relatif:
            print(f"Kelas: {fr[0]}-{fr[1]}, Frekuensi: {fr[2]}, Frekuensi Relatif: {fr[3]:.2f}%")
        print("\nFrekuensi Kumulatif:")
        for fk in self.frekuensi_kumulatif:
            print(f"Kelas: {fk[0]}-{fk[1]}, Frekuensi Kumulatif: {fk[2]}")
        print("\nStatistik Deskriptif:")
        print(f"Rata-rata (Mean): {self.mean_data:.2f}")
        print(f"Median: {self.median_data:.2f}")
        print(f"Standar Deviasi: {self.std_dev_data:.2f}")