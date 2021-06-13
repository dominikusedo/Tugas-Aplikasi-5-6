# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 01:30:03 2021

@author: Dominikus Edo Kristian - 20083000121
"""
jwb = "y"
while jwb=="y" or jwb=="Y":
    print ("==========================")
    print("      CEK TINGKAT USIA ")
    print ("==========================")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input("Masukkan Usia = ")
        if int(u)>0 and int(u)<=100:
            if int(u)>=60: 
                sts="lansia"
            elif int(u)>=35: 
                sts="Dewasa"
            elif int(u)>=18: 
                sts="Pemuda"
            elif int(u)>=15: 
                sts="Remaja"
            else:
                sts="Anak"
            print (sts)
            jwb = input("Cek Ulang? Y/T = ")
            if jwb=="t" or jwb=="T":
                break
        else:
            pesan="Masukkan angka 0-100"
            print(pesan)
            break

