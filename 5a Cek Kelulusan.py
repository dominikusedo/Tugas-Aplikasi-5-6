# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 01:04:40 2021

@author: Dominikus Edo Kristian - 20083000121
"""
jwb = "y"
while jwb=="y" or jwb=="Y":
    print("===================")
    print("   CEK KELULUSAN")
    print("===================")
    n = input("Masukkan Nilai = ")
    if int(n)>60:
        sts = "LULUS"
    else:
        sts = "ULANG"
    print(sts)
    jwb = input("Cek Lagi? Y/T = ")
    if jwb=="t" or jwb=="T":
        break