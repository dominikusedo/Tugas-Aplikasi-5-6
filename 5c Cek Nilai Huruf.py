# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 01:51:46 2021

@author: Dominikus Edo Kristian - 20083000121
"""
jwb = "y"
while jwb=="y" or jwb=="Y":
    print ("==========================")
    print("      CEK NILAI HURUF")
    print ("==========================")
    n=0
    while int(n)>=0 and int(n)<=100:
        n = input("Masukkan Nilai = ")
        if int(n)>=0 and int(n)<=100:
            if int(n)>80: 
                nilai ="BAIK SEKALI"
            elif int(n)>=65: 
                nilai ="BAIK"
            elif int(n)>=55: 
                nilai ="CUKUP"
            elif int(n)>=40: 
                nilai ="KURANG"
            else:
                nilai ="KURANG SEKALI"
            print (nilai)
            jwb = input("Cek Ulang? Y/T = ")
            if jwb=="t" or jwb=="T":
                break
        else:
            pesan="Masukkan nilai 0-100"
            print(pesan)
            break
