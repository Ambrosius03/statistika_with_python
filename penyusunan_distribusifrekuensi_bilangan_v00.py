#data observasi
data = [60, 33, 85, 52, 65, 77, 84, 65, 57, 77,
71, 81, 35, 50, 38, 64, 74, 41, 68, 54,
41, 41, 61, 91, 55, 73, 54, 53, 45, 77,
44, 78, 55, 48, 69, 85, 67, 39, 76, 60,
94, 66, 98, 66, 79, 42, 65, 94, 89, 88]



#nilai terbesar dan terkecil
X = max(data)
Y = min(data)

#banyaknya data
N = len(data)

#range
R = X - Y


#jumlah kelas (aturan sturges)
import math

def sturges_rule(N):
  if N <= 0:
    return 0
  else:
    k = 1 + 3.3 * math.log10(N)
    return round(k)


#panjang kelas
Z = R/sturges_rule(N)
   #bulatkan hasil z(panjang kelas)
import math

h = math.ceil(Z)


#menentukan batas kelas
start = (Y // h) * h # Mulai dari kelipatan h dari nilai minimum

kelas = []
for i in range(sturges_rule(N)):
  lower = start + i * h
  upper = start + (i + 1) * h -1 # Kurangi 1 untuk menghindari tumpang tindih
  kelas.append((lower, upper))





  #hitung frekuensi setiap kelas
frekuensi = []
for lower, upper in kelas:
  count = sum(1 for x in data if lower <= x <= upper)
  frekuensi.append((lower, upper, count))


#frekuensi relatif
frekuensi_relatif = []
for lower, upper, count in frekuensi:
  frekuensi_relatif.append((lower, upper, count, count / N)* 100)

#frekuensi kumulatif
frekuensi_kumulatif = []
total = 0
for lower, upper, count in frekuensi:
  total += count
  frekuensi_kumulatif.append((lower, upper, total))






  #histogram
import matplotlib.pyplot as plt

plt.hist(data, bins=sturges_rule(N), edgecolor='black')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.title('Histogram Data')
plt.show()