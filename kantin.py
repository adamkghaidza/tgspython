# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:02:47 2021

@author: User
"""
"""
1.  Setiap orang/pembeli dapat membeli lebih dari 1 menu makanan dan minuman,
    baik  makanan maupun minuman sekaligus. 
    (Dapat membeli makanan saja atau minuman saja  atau kedua-duanya) 
2.  Terdapat input uang bayar dan hitung kembalian 
3.  Tampilkan menu2 tsb di layar 
4.  Utk OUTPUT tampilkan: menu yg sdh dibeli+harga satuannya+qty+jumlah,  
"""

print("")
print("========================================")
print(" DAFTAR MENU KANTIN FTI")
print("========================================")
print(" MENU MAKANAN ")
print("========================================")
print("a = Nasi Goreng       Rp15.000") 
print("b = Lontong Goreng    Rp14.900")
print("c = Bakso Goreng      Rp12.900") 
print("d = Rujak Goreng      Rp13.000") 
print("e = Rujak Bakso       Rp15.000") 
print("f = Rujak Bakso Pecel Rp17.000") 
print("========================================")
print(" MENU MINUMAN ")
print("========================================")
print("a = Teh Dingin/Hangat/Panas  Rp2.500")
print("b = Kopi Dingin              Rp5.000") 
print("c = Kopi Teh Panas           Rp6.500") 
print("d = Coca Cola Dingin         Rp3.500") 
print("e = Coca Cola                Ro5.000") 
print("========================================")
print("")

#1. variabel makanan
kodemakan = ['a','b','c','d','e','f']
makanan =['Nasi Goreng', 'Lontong Goreng', 'Bakso Goreng', 
           'Rujak Goreng', 'Rujak Bakso', 'Rujak Bakso Pecel']
harga =[15000, 14900, 12900, 13000, 15000, 17000 ]
#2. variabel minuman
kodeminum = ['a','b','c','d','e']
minuman =['Teh Dingin/Panas', 'Kopi Dingin', 'Kopi Teh Panas', 
          'Coca Cola Dingin', 'Coca Cola' ]
harga =[15000, 14900, 12900, 13000, 15000, 17000 ]

#3. Input pilihan
pilihan = input(">> Masukkan Kode Makanan    = ")
pilihan = input(">> Masukkan Kode Minuman    = ")

#4. Input Jumlah
Jumlah = input(">> Masukkan Jumlah Makanan    = ")
Jumlah = input(">> Masukkan Jumlah Minuman    = ")

#5. HITUNG Pembayaran
##cek nama barang dan ambil harga satuan
i = 0
while i<len(makanan,minuman):
    #jika value pada list kode[i] == pilihan
    if kodemakan[i] == pilihan:
        #ambil jenis makanan dan minuman
        nm_brg = makanan[i]

        #ambil harga satuan
        hrgsat = harga[i]
        
    #jika tidak cocok, lanjut ke i berikutnya
    i+=1

tot_byr = hrgsat * int(qty)












