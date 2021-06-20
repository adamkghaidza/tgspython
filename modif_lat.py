# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:50:24 2021

@author: Adam
"""
"""
Buat program untuk menghitung biaya total pengiriman barang di perusahaan Ekspedisi
Lorena di Malang
1. set variabel kota, jarak, ongkirperkm, totongkir
2. input pilihan kota
3. jika kota Sby, jarak = 92, ongkirperkm=2500, 
jika kota Bdg, jarak = 450, ongkirperkm=4000, 
kota Smg, jarak = 365, ongkirperkm=3500
jika kota Jog, jarak = 355, ongkirperkm=3000
4. totongkir = jarak * ongkirperkm
5. tampilkan kota, totongkir
"""
print ("=============================================")
print(" TRANSAKSI BIAYA EKSPEDISI ")
print ("=============================================")
print(" Kode = A. Surabaya")
print(" Kode = B. Bandung")
print(" Kode = C. Semarang")
print(" Kode = D. Yogyakarta")
print ("=============================================")

#Berikut merupakan modifikasi dari ekspedisi dengan tambahan 2 kota,
#yaitu Semarang dan Yogyakarta.

kode =['a','b','c','d']
kota = ['surabaya','bandung','semarang','yogyakarta']
jarak = [92,450,365,355]
ongkirperkm = [2500,4000,3500,3000]

pilihan = input(">> Masukkan Kode Tujuan = ")
#identifikasi pilihan
if pilihan=="a":
    idx = 0
elif pilihan=="b":
    idx = 1
elif pilihan=="c":
    idx = 2
elif pilihan=="d":
    idx = 3    
else:
    idx = 0

#cetak tampilan layar
print(">>> Pilihan Tujuan = " + kota[idx])
print(">>> Jarak          = " + str(jarak[idx]) + " km")
print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))

#hitung transksi
fixjarak = jarak[idx]
fixongkirkm = ongkirperkm[idx]
totongkir = fixjarak * fixongkirkm

#tampilkan total ongkir
print(">>>-------------------------------------")
print(">>> Total Biaya     = Rp." + str(totongkir))
