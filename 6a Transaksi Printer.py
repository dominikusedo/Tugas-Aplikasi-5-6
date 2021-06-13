# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 02:02:44 2021

@author: Dominikus Edo Kristian - 20083000121
"""
jwb = "y"
while jwb=="y" or jwb=="Y":
    print ("=======================================")
    print("NILAI TOTAL TRANSAKSI PRINTER EPSON T20")
    print ("=======================================")
    jml = 1
    hrg = 660000
    while int(jml)>0:
        jml = input("Masukkan Jumlah Printer = ")
        if int(jml)>0:
            Total=int(jml)*int(hrg)
            print("Total Harga Printer = " + str(Total))
            jwb = input("Cek Ulang? Y/T = ")
            if jwb=="t" or jwb=="T":
                break
        else:
            pesan="Masukkan Jumlah Printer"
            print(pesan)
            break