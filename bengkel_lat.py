# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 20:37:35 2021

@author: Adam
"""
"""
Program untuk menghitung biaya total pembelian beberapa merek
oli di perusahaan bengkel motor UD di Malang
1. set variabel merek, pajak, diskon, totbayar
2. pembelian sebelum PPN dengan minimal Rp200000 mendapat diskon
3. Total seluruh pembayaran akan dikenakan pajak 1%
4. input pilihan merek
5. jika merek Duration, diskon = 5%, harga=Rp53000, 
jika merek Castrol , diskon = 5%, harga=Rp50000, 
jika merek Federal, diskon = 5%, harga=Rp54000,
jika merek Yamalube, diskon = 5%, harga=Rp45000,
jika merek Shell, diskon = 5%, harga=Rp46000,
6. totbayar = harga * diskon
7. tampilkan Merek, totbayar
"""
print ("=============================================")
print(" DAFTAR MEREK OLI ")
print ("=============================================")
print(" Kode = A. Duration SW20 1L")
print(" Kode = B. Castrol Magnatec 1L")
print(" Kode = C. Federal Supreme XX 1L")
print(" Kode = D. Yamalube 1L")
print(" Kode = E. Shell 1L")
print ("=============================================")

#Berikut merupakan program menghitung biaya pembelian oli,
#pada bengkel UD di Malang

kode =['a','b','c','d','e']
merek = ['Duration','Castrol','Federal','Yamalube','Shell']
jumlah = [3,2,5,6,4]
harga = [53000,50000,54000,45000,46000]

pilihan = input(">> Masukkan Kode Merek = ")
#identifikasi pilihan
if pilihan=="a":
    idx = 0
elif pilihan=="b":
    idx = 1
elif pilihan=="c":
    idx = 2
elif pilihan=="d":
    idx = 3  
elif pilihan=="e":
    idx = 4
else:
    idx = 0
    
if (harga)<200000
    diskon = (harga) * (5/100)

#diskon
setelah_diskon = (harga) - diskon
print('Diskonnya yaitu : {}'.format(int(diskon)))
print('Harga setelah diskon : {}'.format(int(setelah_diskon)))

#cetak tampilan layar
print(">>> Merek Yang ingin Dipilih = " + merek[idx])
print(">>> Jumlah          = " + str(jumlah[idx]) + " liter")
print(">>> harga           = Rp. " + str(harga[idx]))

#hitung transksi
fixjumlah = jumlah[idx]
fixharga = harga[idx]
totbayar = fixjumlah * fixharga

#tampilkan total biaya
print(">>>-------------------------------------")
print(">>> Total Biaya     = Rp." + str(totbayar))
