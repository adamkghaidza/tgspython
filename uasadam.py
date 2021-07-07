# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 14:17:48 2021

@author: Adam
"""

print("")
print("=================================")
print("APLIKASI MENGHITUNG GAJI CV LOGOS")
print("=================================")
print("Ketentuan Golongan Gaji")
print("Golongan 1  : Rp2.500.000")
print("Golongan 2  : Rp4.500.000")
print("Golongan 3  : Rp6.500.000")
print("================================")
print("Tunjangan Istri")
print("Golongan 1 : 1% Gapok")
print("Golongan 2 : 3% Gapok")
print("Golongan 3 : 5% Gapok")
print("Tunjangan Anak")
print("Semua Golongan : 2% Gapok")
print("================================")
print("")

#1. Variabel Penggajian Karyawan
nama_karyawan = []
golongan = ['1','2','3']
j_kelamin = ['Laki-laki','Perempuan']
status = ['kawin','belum kawin']
tunjistri = []
tunjanak = []
gapok = []

#2. Input Masukan
nama_karyawan = input("Masukkan Nama = ")
golongan = input("Masukkan golongan = ")
j_kelamin = input("Masukkan J.Kelamin =")
status = input("Masukkan Status =")
if golongan == "1" :
    gapok=2500000 
elif golongan == "2" :
     gapok=4500000
elif golongan == "3" :
     gapok=6500000

    
if golongan=="1" :
   tunjangan = (gapok * 0.01)
elif golongan=="2":
     tunjangan = (gapok * 0.03)
elif golongan=="3":
     tunjangan = (gapok * 0.05)
else:
     tunjangan = (gapok * 0.02)

#3. Cek Kondisi
i=0
if j_kelamin == "laki-laki":
    gaji = gapok + tunjistri
elif len (tunjanak)> 1:
    gaji = gapok + tunjanak
gajikotor = ('gapok' + 'tunjanak' + 'tunjistri')    

#4. Perhitungan total
gajikotor = [gapok]
biayajabatan =  gapok * [0.5/100]
pensiun = [gapok - 15500]
organisasi = [gapok - 3500]
totalgaji = (gajikotor + pensiun + organisasi)   

#5. Tampilkan Hasil perhitungan
print("========================================")
print(">>> Nama Karyawan      : " + nama_karyawan + "\r" )
print(">>> Golongan           : " + golongan + "\r")
print(">>> Jenis Kelamin      : " + j_kelamin + "\r")
print(">>> Total Gaji         : Rp " + str (totalgaji) + "\r")
print("========================================")
        
    
    
    
    
